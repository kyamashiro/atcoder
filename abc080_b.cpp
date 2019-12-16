#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int sum;
    int dig;
    int d = n;

    while (d)
    {
        dig = d % 10;
        sum = sum + dig;
        d = d / 10;
    }
    (n % sum == 0) ? cout << "Yes" : cout << "No";
}