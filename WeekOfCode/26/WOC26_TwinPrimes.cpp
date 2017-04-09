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

#include <cmath>
#include <iostream>

using namespace std;

    
void find_primes(bool[], unsigned long long);
unsigned long long answer(bool[], unsigned long long[], unsigned long long);





void find_primes(bool sieve[], unsigned long long size)
{
    // by definition 0 and 1 are not prime numbers
    sieve[0] = false;
    sieve[1] = false;

    // all numbers <= max are potential candidates for primes
    for (unsigned long long i = 2; i <= size; ++i)
    {
        sieve[i] = true;
    }

    // loop through the first prime numbers < sqrt(max) (suggested by the algorithm)
    unsigned int first_prime = 2;
    
    for (unsigned long long i = first_prime; i <= std::sqrt(double(size)); ++i)
    {
        // find multiples of primes till < max
        if (sieve[i] == true)
        {
            // mark as composite: i^2 + n * i 
            for (unsigned long long j = i * i; j <= size; j += i)
            {
                sieve[j] = false;                
            }
        }
    }
}

unsigned long long answer(bool sieve[], unsigned long long n, unsigned long long m)
{
    unsigned long long int sum = 0;
    // all the indexes of the array marked as true are primes
    for (unsigned long long i = n; i <= m-2; ++i)
    { 
        if (sieve[i] == true && sieve[i+2] == true) 
            sum += 1 ;                       
    }
    return sum;
}


int main(){
    unsigned long long n, m;
    std::cin >> n;
    std::cin >> m;
    const unsigned long long max = m+1;
    bool sieve[max];    
    find_primes(sieve, max);
    cout << answer(sieve, n, m) << endl;        
    return 0;
}
