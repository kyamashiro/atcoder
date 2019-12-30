#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cin >> s;

    for (int i = 0; i < s.size(); i++)
    {
        if (!isdigit(s.at(i)))
        {
            cout << "error" << endl;
            return 0;
        }
    }

    cout << stoi(s) * 2 << std::endl;
}