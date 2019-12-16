#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;

    int total;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        int a = x * 2;
        int b = (k - x) * 2;
        a < b ? total += a : total += b;
    }

    cout << total << endl;
}