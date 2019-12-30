#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> m;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        m[num] = num;
    }

    int point = 1;
    int pre = 1;
    int count = 0;
    while (true)
    {
        count++;
        point = pre;
        point = m[point];
        if (point == 2)
        {
            cout << count << endl;
            break;
        }

        if (point == pre)
        {
            cout << -1 << endl;
            break;
        }
    }
}