#include "sort_proc.h"
//#include <algorithm>

// void swap(std::vector<std::string> &items, size_t i, size_t j) {
//   if (i != j) {
//     std::string tmp = items[i];
//     items[i]=items[j];
//     items[j]=tmp;
//   }
// }

// void bubble_sort(std::vector<std::string> &items) {
//   for (size_t i=1; i<items.size(); ++i) {
//     for (size_t j=1; j <= items.size()-i; ++j) {
//       if (items[j]<items[j-1]) {
// 	swap(items,j,j-1);
//       }
//     }
//   }
// }

// void sort_proc(std::vector<std::string> &items) {
//   // TODO sort the items using a procedural programming style in (N log(N)).
//   bubble_sort(items);
// }



void swap(std::string &str1, std::string &str2){
    std::string tmp = str1;
    str1 = str2;
    str2 = tmp; 
}

void partition(std::vector<std::string> &strs, int low_i, int high_i, int &pivot_i){
  //Get Pivot
    pivot_i = high_i;

  //Find Correct position for pivot
    int position = (low_i - 1);
    for(int i=low_i; i<=high_i-1; i++)
    {
        if(strs[i] < strs[pivot_i]){
            position++;
            swap(strs[position],strs[i]);
        }
    }
    swap(strs[position+1], strs[pivot_i]);
    pivot_i = position + 1;
}

void quick_sort(std::vector<std::string> &strs, int low_i, int high_i){
    int pivot_i;
    if(low_i < high_i){
         partition(strs, low_i, high_i, pivot_i);
        //Sort Two Partitions
         quick_sort(strs, low_i, pivot_i-1);
         quick_sort(strs, pivot_i+1, high_i);
    }
}

void sort_proc(std::vector<std::string> &items) {
    quick_sort(items, 0, items.size()-1);

    //std::sort(items.begin(),items.end()); 
    //Tested to see if sort from algorithms library would
    //pass the efficiency test after my attempts failed and 
    //it failed so I gave up at that point.
}
