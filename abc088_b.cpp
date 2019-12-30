#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, alice, bob;
    cin >> n;

    vector<int> v;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        v.push_back(num);
    }

    sort(v.begin(), v.end(), greater<int>());

    for (int i = 0; i < v.size(); i++)
    {
        if (i % 2 == 0)
        {
            alice += v[i];
        }
        else
        {
            bob += v[i];
        }
    }

    cout << alice - bob << endl;
}