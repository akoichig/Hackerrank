#include <iostream>
#include <bits/stdc++.h>
using namespace std;

// https://www.hackerrank.com/contests/projecteuler/challenges/euler027
// https://www.cs.bu.edu/teaching/tool/emacs/programming/

// C++ program to print all primes smaller than or equal to
// n using Sieve of Eratosthenes

void SieveOfEratosthenes(int n)
{
  // Create a boolean array "prime[0..n]" and intialize
  // all entries as true.  A value in prime[i] will
  // finally be false is i is Not a prime, else true
  bool prime[n+1];
  memset(prime, true, sizeof(prime));

  for (int p=2; p*p<=n; p++)
    {
      // If prime[p] is not changed, then it is a prime
      if (prime[p] == true)
	{
	  // Update all multiples of p
	  for (int i=p*2; i<=n; i += p)
	    prime[i] = false;
	}
    }

  // Sum  prime numbers less than or equal to N
  int sum = 0;
  for (int p=2; p<=n; p++)
    if (prime[p])
      sum += p;
      cout << sum << " ";
}

// Driver Program to test above function
int main()
{
  int T;
  int N;
  cin >> T;
  for (int t=1; t<=T; t++)
    {
      cin >> N;
      SieveOfEratosthenes(2*N*N+);
     
    }
  return 0;
}
