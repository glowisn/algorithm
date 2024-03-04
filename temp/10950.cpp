#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int testcase;
    cin >> testcase;

    int *a = new int[testcase];
    int *b = new int[testcase];

    for (int i = 0; i < testcase; i++)
    {
        cin >> a[i] >> b[i];
    }

    for (int i = 0; i < testcase; i++)
    {
        cout << a[i] + b[i] << endl;
    }

    delete[] a;
    delete[] b;
    return 0;
}
