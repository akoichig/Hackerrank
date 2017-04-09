#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <string>
#include <functional>

using namespace std;

template<typename Comparable>
bool isLess(const Comparable & x, const Comparable & y)
{
  if(x.length() < y.length()){
    return true;
      }
  else if(x.length() > y.length()){
    return false;
      }
  else{
    return x<y;
  }
}
 

/**
 * Simple insertion sort.
 */
template <typename Comparable>
void insertionSort( vector<Comparable> & a )
{
    for( int p = 1; p < a.size( ); ++p )
    {
        Comparable tmp = std::move( a[ p ] );

        int j;
        for( j = p; j > 0 && isLess(tmp, a[ j - 1 ]); --j )
            a[ j ] = std::move( a[ j - 1 ] );
        a[ j ] = std::move( tmp );
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
        Comparable tmp = std::move( a[ p ] );
        int j;

        for( j = p; j > left && isLess(tmp, a[ j - 1 ]); --j )
            a[ j ] = std::move( a[ j - 1 ] );
        a[ j ] = std::move( tmp );
    }
}



/**
 * Return median of left, center, and right.
 * Order these and hide the pivot.
 */
template <typename Comparable>
const Comparable & median3( vector<Comparable> & a, int left, int right )
{
    int center = ( left + right ) / 2;
    
    if( isLess(a[ center ], a[ left ]) )
        std::swap( a[ left ], a[ center ] );
    if( isLess(a[ right ], a[ left ]) )
        std::swap( a[ left ], a[ right ] );
    if( isLess(a[ right ], a[ center ]) )
        std::swap( a[ center ], a[ right ] );

        // Place pivot at position right - 1
    std::swap( a[ center ], a[ right - 1 ] );
    return a[ right - 1 ];
}

/**
 * Internal quicksort method that makes recursive calls.
 * Uses median-of-three partitioning and a cutoff of 10.
 * a is an array of Comparable items.
 * left is the left-most index of the subarray.
 * right is the right-most index of the subarray.
 */
template <typename Comparable>
void quicksort( vector<Comparable> & a, int left, int right )
{
    if( left + 10 <= right )
    {
        const Comparable & pivot = median3( a, left, right );

            // Begin partitioning
        int i = left, j = right - 1;
        for( ; ; )
        {
	  while( isLess(a[ ++i ],  pivot) ) { }
	  while( isLess(pivot, a[ --j ]) ) { }
            if( i < j )
                std::swap( a[ i ], a[ j ] );
            else
                break;
        }

        std::swap( a[ i ], a[ right - 1 ] );  // Restore pivot

        quicksort( a, left, i - 1 );     // Sort small elements
        quicksort( a, i + 1, right );    // Sort large elements
    }
    else  // Do an insertion sort on the subarray
        insertionSort( a, left, right );
}

/**
 * Quicksort algorithm (driver).
 */
template <typename Comparable>
void quicksort( vector<Comparable> & a )
{
    quicksort( a, 0, a.size( ) - 1 );
}


int main(){
  int n;
  cin >> n;
  //int n = 12;
  vector<string> unsorted(n);
  //vector<int> unsorted(n);
    for(int unsorted_i = 0; unsorted_i < n; unsorted_i++){
      cin >> unsorted[unsorted_i];
      // unsorted[unsorted_i] = unsorted_i*unsorted_i-unsorted_i-10;
    }
    // your code goes here
    
    // Quicksort
    
    quicksort(unsorted);
   
    
    for (int i = 0; i < n; i++){
      cout << unsorted[i] << endl;
    }
    return 0;
}
