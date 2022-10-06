#include <iostream>

using namespace std;

int *insertionSortR(int *number, int N);

int main(int argc, char const *argv[])
{
    int N;
    int number[1000];
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> number[i];
    }

    insertionSortR(number, N);
    
    for (int i = 0; i < N; i++)
    {
        cout << number[i] << endl;
    }

    return 0;
}

int *insertionSortR(int *number, int N)
{
    if (N > 0)
    {
        insertionSortR(number, N - 1);
        int last = number[N-1];
        int j = N - 2;
        while (j >= 0 && number[j] > last)
        {
            number[j + 1] = number[j];
            j--;
        }
        number[j + 1] = last;
    }
    return 0;
}