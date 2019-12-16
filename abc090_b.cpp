#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    int count;
    for (int i = a; i <= b; i++)
    {
        std::stringstream ss;
        ss << i;
        std::string s = ss.str();
        if(s[0] == s[4] && s[1] == s[3]){
            count++;
        }
    }
    cout << count << endl;
}