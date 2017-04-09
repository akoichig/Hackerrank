// https://www.hackerrank.com/contests/w26/challenges/street-parade-1
// 1<= n<= 10^6 (number of points)
// |a_i| <= 10^9 (coordinates)
// 1 <= h1 <= h2 <= 10^9 (min time, max time)
// 1<= m <= 10^9 (total distance)

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

unsigned long validStart(signed long[] a, unsigned long i){
    // Start in Z(-infty)
        // l0 = length of stay in Z(-infty)
        // h1 <= l0 <= hmax
    if( h1<=m && m<=h2)
        return a[0]-m-1;
    unsigned long start = i;
    unsigned long k = i+1;
    unsigned long l = a[start];
    while(l<m-2*h2)
        l += a[k];
        k ++;
    if(l>m-2*h1)
        return false;
    else
        return true
    // Start >= a0
    
    // Start in Z(infty)?
        
    
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    unsigned long n, m, h1, h2;
    cin >> n;
    
    // Coordinates of borders
    signed long a[n];
    for(unsigned long i = 0; i<n; i++)
         cin >> a[i];
    
    // Distances - NOT NECESSARY
    // What if n=1? Do a brief calculation to figure out where to start in Z(-infty) based on h1, h2, and m
    
    // Assuming n>1
    unsigned int d[n-1];
    for(unsigned long i = 0; i<n-1; i++)
         d[i] = a[i+1]-a[i];
    
    // Boolean arrays for validity of passing through each music zone
    std::vector<bool> notTooShort (n, false);
    std::vector<bool> notTooLong (n, false);

    for(unsigned long i = 0; i<n-1; i++){
        notTooShort[i] = (d[i]>=h1);
        notTooLong[i] = (d[i]<=h2);
    }
    

    
    
    
    unsigned long i = 0;
    while( !validStart(a, i) || i<n)
        i++;
    if(i<n)// Start in zone i, CHECK WHETHER 
        cout << a[i]-h1;
    else
        cout << a[n-1];    
    

    
    // Print d
    for(unsigned long i = 0; i<n-1; i++)
         cout << notTooShort[i] << " and " << notTooLong[i] << endl;

    return 0;
}
