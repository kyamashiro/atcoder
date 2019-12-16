#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, a;
    cin >> n >> a;
    int r = n % 500;
    (r <= a) ? cout << "Yes" : cout << "No";
}