/* 
https://www.hackerrank.com/contests/w26/challenges/twins
Find # of twin prime pairs in interval [n,m].  
1<= n, m <= 10^9
1<= m-n <= 10^6
If there are issues, try using a segmented sieve  
 */

#include <cmath>
#include <iostream>

using namespace std;

    
void find_primes(bool[], unsigned long);
void get_answers(bool[], unsigned long[], unsigned long);
int sum_primes(bool [], unsigned long);




void find_primes(bool sieve[], unsigned long size)
{
    // by definition 0 and 1 are not prime numbers
    sieve[0] = false;
    sieve[1] = false;

    // all numbers <= max are potential candidates for primes
    for (unsigned long i = 2; i <= size; ++i)
    {
        sieve[i] = true;
    }

    // loop through the first prime numbers < sqrt(max) (suggested by the algorithm)
    unsigned int first_prime = 2;
    
    for (unsigned long i = first_prime; i <= std::sqrt(double(size)); ++i)
    {
        // find multiples of primes till < max
        if (sieve[i] == true)
        {
            // mark as composite: i^2 + n * i 
            for (unsigned long j = i * i; j <= size; j += i)
            {
                sieve[j] = false;                
            }
        }
    }
}

void get_answers(bool sieve[], unsigned long n, unsigned long m)
{
    unsigned long int sum = 0;
    // all the indexes of the array marked as true are primes
    for (unsigned long i = n; i <= m-2; ++i)
    { 
        if (sieve[i] == true && sieve[i+2] == true) 
        {
            sum += 1 ;               
        }
        return sum;
        
    }
}


int main(){
    const unsigned long max = 1000;
    bool sieve[max];
    unsigned long n, m;
    find_primes(sieve, max);
    std::cin >> n;
    std::cin >> m;
    cout << answer(sieve, n, m) << endl;    
    }
    return 0;
}

