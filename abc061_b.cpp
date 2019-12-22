#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    map<int, int> arr;

    for (int i = 1; i <= n; i++)
    {
        arr[i] = 0;
    }

    for (int i = 1; i <= m; i++)
    {
        int a, b;
        cin >> a >> b;
        arr[a] += 1;
        arr[b] += 1;
    }

    for (int i = 1; i <= n; i++)
    {
        cout << arr[i] << endl;
    }
}