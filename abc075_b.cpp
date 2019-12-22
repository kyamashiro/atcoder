#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int h, w;
    cin >> h >> w;

    string board[h];

    for (int i = 0; i < h; i++)
    {
        cin >> board[i];
    }

    const int dx[8] = {1, 0, -1, 0, 1, -1, -1, 1};
    const int dy[8] = {0, 1, 0, -1, 1, 1, -1, -1};

    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            if (board[i][j] == '#')
            {
                continue;
            }

            int count = 0;
            for (int k = 0; k < 8; k++)
            {
                int x = i + dx[k];
                int y = j + dy[k];
                if (0 <= x && 0 <= y && x <= w && y <= h)
                {
                    if (board[x][y] == '#')
                    {
                        count++;
                    }
                }
            }
            board[i][j] = char(count + (int)'0');
        }
    }

    for (int i = 0; i < h; i++)
    {
        cout << board[i] << endl;
    }
}
