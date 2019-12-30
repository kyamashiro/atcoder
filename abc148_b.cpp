#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b, n, m;
    cin >> a >> b;

    n = max(a, b);
    m = min(a, b);

    cout << a * b / __gcd(n, m) << endl;
}