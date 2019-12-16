#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<string> vec(n);
    for (int i = 0; i < n; i++)
    {
        cin >> vec.at(i);
    }

    for (string s : vec)
    {
        if (s == "Y")
        {
            cout << "Four";
            std::exit(0);
        }
    }
    cout << "Three" << endl;
}