#pragma once

#include <ranges>
#include <iostream>
#include <vector>
#include <functional>

// Use the "vec" helper functions to write your functional style sort

// vec() -> [], empty list
std::vector<std::string> vec();

// vec(a) -> [a], single element a
std::vector<std::string> vec(const std::string &a);

// vec(a)->a, copy a
std::vector<std::string> vec(const std::vector<std::string> &a);

// vec(a,b)->[a,b], tuple
std::vector<std::string> vec(const std::string &a, const std::string &b);

// vec(a,b)->[a,b[0],..,b[nb-1]], prepend a to b
std::vector<std::string> vec(const std::string &a, const std::vector<std::string> &b);

// vec(a,b)->[a[0],..,a[na-1],b], append b to a
std::vector<std::string> vec(const std::vector<std::string> &a, const std::string &b);

// vec(a,b)->[a[0],..,a[na-1],b[0],..,b[nb-1]], append b to a
std::vector<std::string> vec(const std::vector<std::string> &a, const std::vector<std::string> &b);

// slice(v,b,e)->[v[b],v[b+1],v[b+2],..,v[e-1]], from begin (inclusive) to end (exclusive)
std::vector <std::string> slice(const std::vector < std::string > &a, size_t begin, size_t end);

// swap(v,i,j)->v with values at i and j flipped
std::vector <std::string> swap(const std::vector < std::string > &a, size_t i, size_t j);

// minIndex(v,b,e)->i lowest index i in the range [b,e) that is <= all other elements in range
size_t minIndex(const std::vector < std::string > &a, size_t begin, size_t end);

// print vector on ostream 
template <typename T>
std::ostream& operator<<(std::ostream &out, const std::vector <T> &v) {
  const char *pfx = "[";
  for (const auto &x : v) {
    out << pfx << x;
    pfx=",";
  }
  out << "]";
  return out;
}

// number of arrangements of length m from items (duplication ok)
template <typename T>
int arrangements(const std::vector<T> &items, int len) {
    return (int) pow(items.size(),len);
}

// i'th arrangment
template <typename T>
std::vector < T > arrangement(const std::vector< T > &items, int len, int i) {
  std::vector < std::string > ans(len,"");
  for (int k=0; k<len; ++k) {
    ans[k] = items[i % items.size()];
    i = i / items.size();
  }
  return ans;
}

#define STRING(x) ([&]() { std::ostringstream oss; oss << x; return oss.str(); })()
