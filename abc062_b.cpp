#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int h, w;
    cin >> h >> w;

    vector<string> vec;
    for (int i = 0; i < h; i++)
    {
        string s;
        cin >> s;
        vec.push_back(s);
    }

    string edge;
    for (int i = 0; i < w + 2; i++)
    {
        edge += '#';
    }

    cout << edge << endl;
    for (int i = 0; i < h; i++)
    {
        cout << '#' << vec.at(i) << '#' << endl;
    }
    cout << edge << endl;
}
