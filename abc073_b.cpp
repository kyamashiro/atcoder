#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<pair<int, int>> vec;
    for (int i = 0; i < n; i++)
    {
        int s1;
        int s2;
        cin >> s1 >> s2;
        vec.push_back({s1, s2});
    }

    int count = 0;
    for (pair<int, int> p : vec)
    {
        count += p.second - p.first + 1;
    }
    cout << count << endl;
}