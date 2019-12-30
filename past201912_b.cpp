#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    array<int, 100000> arr;
    for (int i = 0; i < n; i++)
    {
        int n;
        cin >> n;
        arr[i] = n;
    }

    int pre = arr[0];
    for (int i = 1; i < n; i++)
    {
        int today = arr[i];
        if (today == pre)
        {
            cout << "stay" << endl;
        }

        if (pre < today)
        {
            cout << "up " << today - pre << endl;
        }

        if (today < pre)
        {
            cout << "down " << pre - today << endl;
        }

        pre = today;
    }
}