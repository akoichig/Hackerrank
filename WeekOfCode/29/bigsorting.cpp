#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;


bool is_not_digit(char c){
    return !isdigit(c);
}



/** 
 * Quicksort algorithm (driver)
 */

template <typename Comparable>
void quicksort( vector<Comparable> & a)
{
  quicksort( a, 0, a.size() - 1);
}

/**
 * Return the median of left, center, and right.
 * Order these and hide the pivot.
 */

template<typename Comparable>
const Comparable & median3( vector<Comparable> & a, int left, int right )
{
  int center = ( left + right ) / 2;

  if(a[center] < a[left])
    std::swap(a[left], a[center]);
  if(a[right] < a[left])
    std::swap(a[left], a[right]);
  if(a[right]<a[center])
    std::swap(a[center], a[right]);

  // Place pivot at position right - 1
  std::swap(a[center], a[right - 1]);
  return a[right - 1];
}

/** 
 * Simple insertion sort.
 */
template <typename Comparable>
void insertionSort( vector<Comparable> & a)
{
  for( int p=1; p<a.size(); ++p)
    {
      Comparable tmp = move(a[p]);

      int j;
      for(j=p; j>0 && tmp<a[j-1]; --j)
          a[j] = move(a[j-1]);
      a[j] = move(tmp);
    }
}


/**
 * Internal insertion sort routine for subarrays
 * that is used by quicksort.
 * a is an array of Comparable items.
 * left is the left-most index of the subarray.
 * right is the right-most index of the subarray.
 */
template <typename Comparable>
void insertionSort( vector<Comparable> & a, int left, int right )
{
    for( int p = left + 1; p <= right; ++p )
    {
        Comparable tmp = move( a[ p ] );
        int j;

        for( j = p; j > left && tmp < a[ j - 1 ]; --j )
            a[ j ] = move( a[ j - 1 ] );
        a[ j ] = move( tmp );
    }
}

/** 
 * Internal quicksort method that makes recursive calls.
 * Uses median-of-three partitioning and a cutoff of 10.
 * a is an array of Comparable items.
 * left is the left-most index of the subarray.
 * right is the right-most index of the subarray.
 */

template <typename Comparable>
void quicksort( vector<Comparable> & a, int left, int right)
{
  if(left+10 <= right)
    {
      const Comparable & pivot = median3(a, left, right);

      // Begin partitioning
      int i = left, j = right - 1;
      for( ; ; )
	{
	  while(a[ ++i ] < pivot ){}
	  while(pivot < a[--j]) {}
	  if( i < j)
	    swap(a[i], a[j]);
	  else
	    break;
	}

      swap(a[i], a[right - 1]); // Restore pivot

      quicksort(a, left, i-1); // Sort small elements
      quicksort(a, i+1, right); // Sort large elements
    }
  else // Do an insertion sort on the subarray
    insertionSort(a, left, right);
}



int main(){
    int n;
    cin >> n;
    vector<string> unsorted(n);
    for(int unsorted_i = 0; unsorted_i < n; unsorted_i++){
       cin >> unsorted[unsorted_i];
    }
    // your code goes here
    
    // Quicksort
    
    //quicksort(unsorted, 0, n);
    median3(unsorted, 0, n);
    
    for (int i = 0; i < n; i++){
        cout << unsorted[i] << endl;
    }
    return 0;
}
