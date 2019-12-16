#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, k;
    cin >> n >> k;
    int c = 1;

    while (n)
    {
        ((c * 2) < (c + k)) ? c *= 2 : c += k;
        n--;
    }

    cout << c << endl;
}