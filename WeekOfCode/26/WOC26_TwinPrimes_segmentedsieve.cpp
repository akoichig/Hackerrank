/* 
https://www.hackerrank.com/contests/w26/challenges/twins
Find # of twin prime pairs in interval [n,m].  
1<= n, m <= 10^9
1<= m-n <= 10^6

Change size to m?

If there are issues, try using a segmented sieve  
Get segmentation fault (core dumped) with n=8e6 m=9e6
Try using segmented sieves of size 10000
Let bool represent n to m.

what should be ans for following test cases 1)1,1000000 2)10000,1000000000 3)203,10001 please reply

For the first test case answer is = 8169 second one is not valid because |m-n|<10^6 For the third one answer is = 190 For the test case 999000000 1000000000 answer is = 3063 (i think this is the worst test case.) :D

 */


#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <stdint.h>

using namespace std;

// Segmented Sieve http://primesieve.org/segmented_sieve.html by Kim Walisch

/// Set your CPU's L1 data cache size (in bytes) here
const int L1D_CACHE_SIZE = 32768;

/// Generate primes using the segmented sieve of Eratosthenes.
/// This algorithm uses O(n log log n) operations and O(sqrt(n)) space.
/// @param limit  Sieve primes <= limit.
///
void segmented_sieve(int64_t limit, int64_t N)
{
  int sqrt = (int) std::sqrt(limit);
  int segment_size = std::max(sqrt, L1D_CACHE_SIZE);

  //int64_t count = (limit < 2) ? 0 : 1; // used for counting primes
  int64_t twincount = 0;
  int64_t s = 3;
  int64_t n = 3;

  // generate small primes <= sqrt
  std::vector<char> is_prime(sqrt + 1, 1);
  for (int i = 2; i * i <= sqrt; i++)
    if (is_prime[i])
      for (int j = i * i; j <= sqrt; j += i)
        is_prime[j] = 0;

  // vector used for sieving
  std::vector<char> sieve(segment_size);
  std::vector<int> primes;
  std::vector<int> next;

  for (int64_t low = 0; low <= limit; low += segment_size)
  {
    std::fill(sieve.begin(), sieve.end(), 1);

    // current segment = interval [low, high]
    int64_t high = std::min(low + segment_size - 1, limit);

    // add new sieving primes <= sqrt(high)
    for (; s * s <= high; s += 2)
    {
      if (is_prime[s])
      {
        primes.push_back((int) s);
          next.push_back((int)(s * s - low));
      }
    }
    
    // sieve the current segment
    for (std::size_t i = 0; i < primes.size(); i++)
    {
      int j = next[i];
      for (int k = primes[i] * 2; j < segment_size; j += k)
        sieve[j] = 0;
      next[i] = j - segment_size;
    }

    /* Original prime counter
    for (; n <= high; n += 2){
      if (sieve[n - low]) // n is a prime
	{
        count++;
	cout << n << endl;
      }
    }
    */
    
    int64_t start = std::max(int64_t(3), N);
    if(start % 2 == 0)
      start ++;
    for (n = start; n <= high-2; n += 2){
      if (sieve[n - low] && sieve[n+2-low]){ // n is a prime
	//std::cout << n << " and " << n+2 << "  are twin primes. " << std::endl;
        twincount++;
      }
    }
    
      
  }
    
  //std::cout << count << " primes found." << std::endl;
  //std::cout << sieve[0] << " " << sieve[1] << " " << sieve[2] << std::endl;
  std::cout << twincount << endl;
}


// END Segmented Sieve


int main(){
    int64_t n;
    int64_t m;
    std::cin >> n;
    std::cin >> m;
    //const unsigned long max = m+1;
    //bool sieve[max];    
    //find_primes(sieve, max);
    //cout << answer(sieve, n, m) << endl;
    segmented_sieve(m, n);
    return 0;
}



