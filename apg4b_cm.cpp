#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    string sa = "A:";
    string sb = "B:";
    for (int i = 0; i < a; i++)
    {
        sa += "]";
    }

    for (int i = 0; i < b; i++)
    {
        sb += "]";
    }

    cout << sa << endl
         << sb << endl;
}