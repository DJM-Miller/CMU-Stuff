#include <cmath>
#include <chrono>
#include <thread>
#include <iostream>
#include <vector>
#include <string>

#include "utility.h"
#include "sort_proc.h"
#include "gtest/gtest.h"

// There are other clocks, but this is usually the one you want.
// It corresponds to CLOCK_MONOTONIC at the syscall level.
using Clock = std::chrono::steady_clock;
using std::chrono::time_point;
using std::chrono::duration_cast;
using std::chrono::milliseconds;
using namespace std::literals::chrono_literals;
using std::this_thread::sleep_for;

using namespace std;

const std::string letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

void randomize(std::string &s, size_t size) {
  s.resize('?',size);
  for (int i=0; i<size; ++i) {
    s[i]=letters[rand() % letters.size()];
  }
}

void randomize(std::vector<std::string> &v, size_t size) {
  v.resize(size);
  for (size_t i=0; i<size; ++i) {
    randomize(v[i],rand() % 20);
  }
}

TEST(Sort,Efficiency) {
  std::vector<std::string> v;
  std::vector< std::pair < size_t , double > > times;
  for (auto n : { 10, 100, 1000, 10'000, 100'000, 1'000'000 }) {
    randomize(v,n);
    std::vector<std::string> w(v);
    time_point<Clock> start0 = Clock::now();    
    std::sort(w.begin(),w.end());
    time_point<Clock> end0 = Clock::now();
    double time0 = duration_cast<milliseconds>(end0 - start0).count()/1000.0;
    
    std::cout << "sort case n=" << n << std::endl;
    time_point<Clock> start = Clock::now();
    sort_proc(v);
    time_point<Clock> end = Clock::now();
    double time = duration_cast<milliseconds>(end - start).count()/1000.0;

    ASSERT_EQ(v,w);

    std::cout << "sorted " << n << " items in " << time << "seconds" << std::endl;

    times.push_back(std::pair(n,time));
    if (times.size() >= 2) {
      double x0 = times[times.size()-2].first;
      double y0 = times[times.size()-2].second;
      double x1 = times[times.size()-1].first;
      double y1 = times[times.size()-1].second;

      double c1 = (y1-y0)/(x1*log(x1)-x0*log(x0));

      std::cout << "c1 about " << c1 << std::endl;

      ASSERT_TRUE(c1 < 1e-4) << "c1 = " << c1 << " for n = " << n;
      ASSERT_TRUE(y1 < 1000.0*time0)  << " 1000x slower than standard sort";
    }
  }
}
