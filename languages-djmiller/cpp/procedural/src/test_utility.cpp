#include <cmath>
#include <vector>
#include <string>
#include <sstream>
#include "gtest/gtest.h"

#include "utility.h"

TEST(Utility,VectorPrint) {
    std::ostringstream oss;
    std::vector < std::string > a = { "x", "y", "z" };
    oss << a;
    std::string equiv = oss.str();
    ASSERT_EQ("[x,y,z]",equiv);
}

TEST(Utility,STRING) {
    std::vector < std::string > a = { "x", "y", "z" };
    ASSERT_EQ("[x,y,z]",STRING(a));

}

// Test that arrangements are correct
TEST(Utility,Arrangements) {
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
