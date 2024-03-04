#include <iostream>

int d(int n){
    int sum = n;
    for(int i = 0; i < 5; i++){
        sum += n % 10;
        n /= 10;
    }

    return sum;
}

int main(){
    bool gener[10001];

    for(int i = 1;i <= 10000; i++){
        gener[i] = true;
    }

    for(int i = 1;i <= 10000; i++){
        gener[d(i)] = false;
    }

    for(int i = 1;i <= 10000; i++){
        if(gener[i] == true){
            std::cout << i << std::endl; 
        }
    }

    return 0;
}