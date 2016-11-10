#include<iostream>
#include<chrono>
#include<thread>
#include<mutex>
#include<atomic>

#define NUM_SIZE 100000000

using namespace std;
using namespace std::chrono;

class TimeCheck
{
public:
	TimeCheck() {};
	~TimeCheck() {};

	void checkStart() { start = high_resolution_clock::now(); }
	void CheckEnd() { end = high_resolution_clock::now(); }
	void ShowDurationTime() { cout << "Computing time is " << duration_cast<milliseconds>(end-start).count() << "ms, "; }
	
private:
	high_resolution_clock::time_point start;
	high_resolution_clock::time_point end;
};

TimeCheck t;
int volatile sum{ 0 };
void func(int core) { for (int i = 0; i < (NUM_SIZE / core); ++i) { sum += 1; } }

bool volatile flag[2]{ false,false };
int volatile turn{ 0 };
void func_dekker_0() {
	for (int i = 0; i < NUM_SIZE/2; ++i)
	{
		flag[0] = true;
		while (flag[1] == true) {
			if(turn == 1) {
				flag[0] = false;
				while (turn == 1);
				flag[0] = true;
			}
		}
		++sum;
		turn = 1;
		flag[0] = false;
		
	}
}
void func_dekker_1() {
	for (int i = 0; i < NUM_SIZE/2; ++i)
	{
		flag[1] = true;
		while (flag[0] == true) {
			if (turn == 0) {
				flag[1] = false;
				while (turn == 0);
				flag[1] = true;
			}
		}
		++sum;
		turn = 0;
		flag[1] = false;

	}
}
mutex mylock;
void func_mutex(int core) {
	for (int i = 0; i < (NUM_SIZE / core); ++i) {
		mylock.lock();
		sum += 1;
		mylock.unlock();
	}
}

atomic<int> atomic_sum{ 0 };
void func_atomic(int core) { for (int i = 0; i < (NUM_SIZE / core); ++i) { atomic_sum += 1; } }

atomic_flag TAS_lock = ATOMIC_FLAG_INIT;
void func_TAS(int core) {
	for (int i = 0; i < (NUM_SIZE / core); ++i) {
		while (atomic_flag_test_and_set(&TAS_lock));
		sum += 1;
		atomic_flag_clear(&TAS_lock);
	}
}

int main()
{
	cout << "Q1\n";
	t.checkStart();
	func(1);
	t.CheckEnd();
	t.ShowDurationTime();
	cout << "Number of Thread = 1,\tSUM =" << sum << endl;
	sum = 0;

	int threads{ 1 }, i{ 0 };
	thread *threadList[16];

	cout << "Q2\n";
	for (threads = 1; threads <= 16; threads *= 2) {
		for (int i = 0; i < threads; ++i) {
			thread *tempThread = new thread{ func,threads };
			threadList[i] = tempThread;
		}
		t.checkStart();
		for (int i = 0; i < threads; ++i) {
			threadList[i]->join();
			delete threadList[i];

		}
		t.CheckEnd();
		t.ShowDurationTime();
		cout << "Number of Thread =" << threads << ",\tSUM =" << sum << endl;
		sum = 0;
	}

	cout << "Q3\n";
	thread t1{ func_dekker_0 };
	thread t2{ func_dekker_1 };
	t.checkStart();
	t1.join();
	t2.join();
	t.CheckEnd();
	t.ShowDurationTime();
	cout << "Number of Thread =2,\tSUM =" << sum << endl;
	sum = 0;


	cout << "Q4\n";
	for (threads = 1; threads <= 16; threads *= 2) {
		for (int i = 0; i < threads; ++i) {
			thread *tempThread = new thread{ func_mutex,threads };
			threadList[i] = tempThread;
		}
		t.checkStart();
		for (int i = 0; i < threads; ++i) {
			threadList[i]->join();
			delete threadList[i];
		}
		t.CheckEnd();
		t.ShowDurationTime();
		cout << "Number of Thread =" << threads << ",\tSUM =" << sum << endl;
		sum = 0;
	}

	cout << "Q5\n";
	for (threads = 1; threads <= 16; threads *= 2) {
		for (int i = 0; i < threads; ++i) {
			thread *tempThread = new thread{ func_atomic,threads };
			threadList[i] = tempThread;
		}
		t.checkStart();
		for (int i = 0; i < threads; ++i) {
			threadList[i]->join();
			delete threadList[i];
		}
		t.CheckEnd();
		t.ShowDurationTime();
		cout << "Number of Thread =" << threads << ",\tSUM =" << atomic_sum << endl;
		atomic_sum = 0;
	}


	cout << "Q6\n";
	for (threads = 1; threads <= 16; threads *= 2) {
		for (int i = 0; i < threads; ++i) {
			thread *tempThread = new thread{ func_TAS,threads };
			threadList[i] = tempThread;
		}
		t.checkStart();
		for (int i = 0; i < threads; ++i) {
			threadList[i]->join();
			delete threadList[i];
		}
		t.CheckEnd();
		t.ShowDurationTime();
		cout << "Number of Thread =" << threads << ",\tSUM =" << sum << endl;
		sum = 0;
	}
}