#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n = 6;

    vector<int> vec;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        vec.push_back(num);
    }

    sort(vec.begin(), vec.end());

    cout << vec.at(3) << endl;
}