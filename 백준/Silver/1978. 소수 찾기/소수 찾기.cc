#include <iostream>

using namespace std;

int main()
{
   bool pa[1001];
   pa[1] = false;
   for(int i = 2; i <= 1000; i++){
       pa[i] = true;
   } 
   for(int i = 0; i < 1000; i++){
       if(pa[i]){
           for(int j = i * i; j <= 1000; j += i){
               pa[j] = false;
           }
       }
   }

   int n;
   cin >> n;
   int* input = new int[n];
   for(int i = 0; i < n; i++){
       cin >> input[i];
   }
   int cnt = 0;

   for(int i = 0; i < n ; i++){
       if(pa[input[i]]){
           cnt++;
       }
   }

    cout << cnt;

    return 0;
}