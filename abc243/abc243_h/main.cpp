#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;

constexpr int64_t MOD = 998244353;
const std::string YES = "Yes";
const std::string NO = "No";
auto solve(auto H, auto W, const std::vector<std::vector<auto> > &C) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    auto H, W;
    std::cin >> H >> W;
    std::vector<std::vector<auto> > C(H + W + 4, std::vector<auto>((H + W + 4)));
    REP (j, H + 4) {
        REP (i, W) {
            std::cin >> C[i + j][i + j];
        }
    }
    auto ans = solve(H, W, C);
    std::cout << Yes << '\n';
    std::cout << n << ' ' << r << '\n';
    return 0;
}
