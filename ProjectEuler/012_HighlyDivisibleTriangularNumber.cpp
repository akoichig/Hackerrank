#include <cmath>
#include <iostream>

using namespace std;
// k = 41040, T_k = 842161320, numDiv = 1024, which is 26th record-breaker
    
unsigned int numDiv(unsigned int n);
unsigned int get_answer(unsigned int n);
unsigned int * helperMemory;
unsigned int * memo_T;
unsigned int * memo_Tdiv;
unsigned limit = 42000;


int main(){
  int max = 0;
  int listcnt = 0;

  helperMemory = new unsigned int[limit];
  memo_T = new unsigned int[limit];
  memo_Tdiv = new unsigned int[limit];
  for(int i = 0; i<limit; i++)
    {
      helperMemory[i] = 0;
      memo_T[i]= 0;
      memo_Tdiv[i]= 0;
    }


  
  for(int k=1; k<limit; k++){
    int T = k*(k+1)/2;
    int ndiv1;
    int ndiv2;
    int ndiv;
    if(k%2==0){
      ndiv1 = numDiv(k/2);
      ndiv2 = numDiv(k+1);      
    }
    else{
      ndiv1 = numDiv((k+1)/2);
      ndiv2 = numDiv(k);      
    }    
    ndiv = ndiv1*ndiv2;
    if(T<limit){
      helperMemory[T] = ndiv;
    }
    if(ndiv > max){
      memo_T[listcnt] = T;
      memo_Tdiv[listcnt] = ndiv;
      listcnt ++;
      max = ndiv;
    }

  }
  
  int t;
  std::cin >> t;
  for(int a0 = 0; a0 < t; a0++){
    unsigned int n;
    std::cin >> n;
    cout << get_answer(n) << endl;
  }
  return 0;
  
}


unsigned int numDiv(unsigned int n){
  if(helperMemory[n] == 0){
    unsigned int limit = n;
    unsigned int num = 0;
    if ( n == 1)
      return 1;
    int i = 1;
    while (i < limit){
      if (n % i == 0){
	limit = n / i;
	if (limit != i){
	  num += 1;
	}
	num += 1;     
      }
      i += 1;
    }
    helperMemory[n] =  num;
  }
  return helperMemory[n];
}


// 376, 641

  
unsigned int get_answer(unsigned int n){
  int k;
  k = 1;
  //cout << "DEBUG: (get_answer) n = " << n << endl;
  while(memo_Tdiv[k]<=n){
    k++;
  }
  return memo_T[k];
}

