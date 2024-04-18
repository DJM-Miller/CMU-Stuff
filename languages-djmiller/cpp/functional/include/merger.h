#pragma once

#include <vector>

// merging collection which iterates through a sequence of two orderd collections
template <typename CItA, typename CItB, typename Ordered = std::less < typename CItA::value_type > >
struct merger {
  Ordered ordered;
  const CItA a0;
  const CItA a1;
  const CItB b0;
  const CItB b1;

  merger(const CItA &_a0,const CItA &_a1,const CItB &_b0,const CItB &_b1) 
   : a0(_a0), a1(_a1), b0(_b0), b1(_b1) {}
  
  struct const_iterator {
    using iterator_category = std::forward_iterator_tag;
    using difference_type   = std::ptrdiff_t;
    using value_type        = typename CItA::value_type;
    using pointer           = typename CItA::value_type*;
    using reference         = typename CItA::value_type&;

    const merger &m;
    CItA a;
    CItB b;

    const_iterator(const merger &_m, const CItA &_a,const CItB &_b) 
     : m(_m), a(_a), b(_b) 
     {
     }

    bool flipped() const {
      return (b != m.b1 && (a == m.a1 || m.ordered(*b,*a)));
    }

    const value_type & operator*() const { return flipped() ? *b : *a; }
    const value_type * operator->() { return flipped() ? b : a; }
    const_iterator& operator++() { if (flipped()) ++b; else ++a; return *this; }  
    const_iterator operator++(int) { const_iterator tmp(*this); ++(*this); return tmp; }
    friend difference_type operator-(const const_iterator &begin, const const_iterator &end) { return (end.a-begin.a)+(end.b-begin.b); }
    friend bool operator== (const const_iterator& x, const const_iterator& y) { return x.a == y.a && x.b == y.b; };
    friend bool operator!= (const const_iterator& x, const const_iterator& y) { return ! ( x == y); }
  };

  const_iterator begin() const { return const_iterator(*this,a0,b0); }
  const_iterator end() const { return const_iterator(*this,a1,b1); }
  const_iterator cbegin() const { return const_iterator(*this,a0,b0); }
  const_iterator cend() const { return const_iterator(*this,a1,b1); }
};
