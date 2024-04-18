#include <cmath>
#include <vector>
#include "gtest/gtest.h"

#include "merger.h"

TEST(Merger,Int) {
    std::vector < int > a = { 10, 20, 30 };
    std::vector < int > b = { 9, 10, 22, 31 };
    std::vector < int > expect = { 9, 10, 10, 20, 22, 30, 31 };

    merger m(a.begin(), a.end(), b.begin(), b.end());

    auto i = expect.begin();
    auto j = m.begin();

    for (;;) {
        if (i == expect.begin()) {
            ASSERT_EQ(j,m.begin());
        } else {
            ASSERT_NE(j,m.begin());
        }
        if (i == expect.end()) {
            ASSERT_EQ(j,m.end());
            break;
        } else {
            ASSERT_NE(j,m.end());
        }
        ASSERT_EQ(*i,*j);
        ++i;
        ++j;
    }
}