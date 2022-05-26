#include <iostream>

using namespace std;

int main()
{
    long long N;
    cin >> N;
    long long M = 1;

    while (M < N)
    {
        M = M * 2 + 1;
    }
    if (M == N)
    {
        cout << 1 << endl
             << N << endl;
    }
    else
    {
        cout << 2 << endl
             << (M ^ N) << endl
             << N << endl;
    }

    return 0;
}