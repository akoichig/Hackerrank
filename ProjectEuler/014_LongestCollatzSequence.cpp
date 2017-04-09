// algorithm, vector, cstdio
// Using int, cases 0 through 4 passed
#include <cmath>
#include <iostream>
#include <map>

using namespace std;
unsigned long limit1 = 15000002; // used 5e6 as limit, try 3(5e6)+1
unsigned long limit = 5000000; // used 5e6 as limit, try 3(5e6)+1
unsigned long * memo_next;
unsigned long * memo_len;
unsigned long * path;
unsigned long lastVisited = 1;

unsigned long nextTerm(unsigned long n){
  if(n%2==0)
    return n/2;
  else
    return 3*n+1;
}

unsigned long lenCollatz(unsigned long n){
  if(n==1)
    return 0;
  if(memo_len[n]!=0){
    unsigned long pathlen = 1;
    unsigned long k = n;
    while(k!=1 || memo_len[k]!=0){
      path[pathlen] = k;
      pathlen ++;
      k = memo_next[k];
    }
    // if k==1
    for(unsigned long i=pathlen; i!=0; i--){
      memo_len[path[i]] = pathlen-i;
    }
    // if memo_len[k] != 0 (maybe unifiable)
    unsigned long start = memo_len[k];
    for(unsigned long i=pathlen-1; i!=0 i--){
      start ++;
      memo_len[path[i]] = start;
    }
  }
  return memo_len[n];
}


int main(){//prepare
  memo_next = new unsigned long[limit1];
  memo_len = new unsigned long[limit1];
  path = new unsigned long[limit];
  unsigned long maxl = 0;
  unsigned long l;
  unsigned long maxk;

  for(unsigned long i = 1; i<limit1/2; i++)
    memo_next[2*i] = i;
  for(unsigned long i = 1; i<(limit-1)/2; i++)
      memo_next[2*i+1] = 6*i+4;
  for(unsigned long i = 2; i<limit1; i+=2){
    l = lenCollatz(i);
    if(l>=maxl){
      unsigned
	// unfinished, but scan memo_len and keep track of len>=maxlen -> update maxk, filling in memo_ans along the way

    }
  }

    // somehow store lengths
  /* PRINT SOME ENTRIES
    for(unsigned long i = 1; i<limit; i++)
    if(memo_next[i]==0)
      cout<<"i = "<<i<< " maps to 0." << endl;
  */
  return 0;
}

// blank ones have i = 6q+4>= limit
// i-1 >= limit-1
// (i-1)/3  >= (limit-1)/3
// (limit-1)/3 rounds down to 1,666,666

int main2(){
  int t = 10;
  unsigned long i;
  for(int a0=0; a0<t; a0++){
    std::cin >> i;
    cout << "Doubling: " << 2*i << endl;
    if(i%6==4){
      cout << "i=4mod6 : " << (i-1)/3 << endl;
    }
  }  
  return 0;
}

// memo_next[1] = 0
// scan through map, visiting all i==4mod 6 (10, 16, 22, ...) and do
//                memo_next[(i-1)/3] = i (remaining empty odd indices required i>limit)
// rescan map, visiting all i and do
//                memo_next[2*i] = i (all even indices get defined)
// Try visiting (i-1)/3 first; then double.
//
// fill in lengths? Or wait until needed?
// simultaneously, determine answer

