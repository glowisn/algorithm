#include <iostream>

using namespace std;

int gcd(int a, int b);
int lcm(int a, int b, int mi);

int main()
{
    int a, b;

    cin >> a >> b;

    int mi = gcd(a,b);

    cout << mi << endl << lcm(a,b,mi);
    
    return 0;
}

int gcd(int a, int b){
    return b ? gcd(b, a % b) : a;
}

int lcm(int a, int b ,int mi){
    return (a / mi) * b;
}