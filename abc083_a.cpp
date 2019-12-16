#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    (a + b == c + d) ? cout << "Balanced" : (a + b < c + d) ? cout << "Right" : cout << "Left";
}