#include <bits/stdc++.h>
using namespace std;

int main()
{
    string n;
    cin >> n;
    ((n[0] == n[1] && n[0] == n[2]) || (n[3] == n[1] && n[3] == n[2])) ? cout << "Yes" : cout << "No";
}