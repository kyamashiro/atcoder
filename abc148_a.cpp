#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    if (a + b == 3)
    {
        cout << 3 << endl;
        exit(0);
    }

    if (a + b == 4)
    {
        cout << 2 << endl;
        exit(0);
    }

    cout << 1 << endl;
}