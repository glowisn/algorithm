#include <iostream>
using namespace std;

int main(){
    int n ,m;
    int num[101];
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        cin >> num[i];
    }

    int sum = 0;
    int max = -1;
    for(int i = 1; i <= n; i++){\
        for(int j = i + 1 ; j <= n ;j++){
            for(int k = j +1; k <=n; k++){
                sum = num[i] + num[j] + num[k];
                if(sum > max && sum <= m){
                    max = sum;
                }
                sum = 0;
            }
        }
    }
    cout << max << endl;
    return 0;
}