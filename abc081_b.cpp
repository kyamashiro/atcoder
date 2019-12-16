#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> vec;
    for (int i = 0; i < n; i++)
    {
        int a;
        cin >> a;
        vec.push_back(a);
    }

    int count;
    while (true)
    {
        for (int i = 0; i < vec.size(); i++)
        {
            if (vec[i] % 2 == 0)
            {
                vec[i] = vec[i] / 2;
            }
            else
            {
                cout << count << endl;
                exit(0);
            }
        }
        count++;
    }

    cout << count << endl;
}