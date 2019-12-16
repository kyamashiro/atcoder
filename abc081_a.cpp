#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int count = 0;
    s[0] == '1' ? count++ : 0;
    s[1] == '1' ? count++ : 0;
    s[2] == '1' ? count++ : 0;

    cout << count;
}