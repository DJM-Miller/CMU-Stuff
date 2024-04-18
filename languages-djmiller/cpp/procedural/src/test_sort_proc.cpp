#include <cmath>
#include "sort_proc.h"
#include "gtest/gtest.h"
#include "utility.h"

using namespace std;

// sample items to test on
const std::vector < std::string> samples = { 
      "", " ", "1", "11", "2", "a", "apple", "cart"
};


// Test that arrangements are correct
TEST(Sort,Arrangements) {
  std::vector < std::string > s1 = {"x"};
  std::vector < std::string > s3 = {"x","y","z"};

  ASSERT_EQ(1,arrangements(s1,4));
  ASSERT_EQ(81,arrangements(s3,4));
  
  std::vector < std::string > s3_0 = {"x","x","x","x"};
  std::vector < std::string > s3_1 = {"y","x","x","x"};
  std::vector < std::string > s3_2 = {"z","x","x","x"};
  std::vector < std::string > s3_3 = {"x","y","x","x"};
  std::vector < std::string > s3_9 = {"x","x","y","x"};
  std::vector < std::string > s3_80 = {"z","z","z","z"};

  ASSERT_EQ(s3_0,arrangement(s3,4,0));
  ASSERT_EQ(s3_1,arrangement(s3,4,1));
  ASSERT_EQ(s3_2,arrangement(s3,4,2));
  ASSERT_EQ(s3_3,arrangement(s3,4,3));
  ASSERT_EQ(s3_9,arrangement(s3,4,9));
  ASSERT_EQ(s3_80,arrangement(s3,4,80));
}

// test procedural style; all arrangments of samples, len < 4
TEST(Sort, Proc) {
  std::vector < std::string > items = {};
  std::vector < std::string > expect = {};
  std::vector < std::string> result;

  for (int len = 0; len < 4; ++len) {
    int n = arrangements(samples,len);
    for (int i = 0; i < n; ++i) {
      auto items = arrangement(samples,len,i);

      std::vector < std::string > expect(items);
      std::sort(expect.begin(),expect.end());

      std::vector < std::string > result(items);

      sort_proc(result);

      ASSERT_EQ(expect,result) << " for items = " << items;
    }
  }
}
