#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, m;
    cin >> n;

    map<string, int> mp;

    for (int i = 0; i < n; i++)
    {
        string val;
        cin >> val;
        mp[val] += 1;
    }

    cin >> m;
    for (int i = 0; i < m; i++)
    {
        string val;
        cin >> val;
        mp[val] -= 1;
    }

    int max = mp.begin()->second;
    for (auto itr = mp.begin(); itr != mp.end(); ++itr)
    {
        if (max < itr->second)
        {
            max = itr->second;
        }
    }

    max < 0 ? cout << 0 : cout << max;
}
