#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;

constexpr int64_t MOD = 1000000007;
int64_t solve(auto a, const std::vector<auto> &b, const std::vector<auto> &c, auto d) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    auto a, d;
    std::cin >> a;
    std::vector<auto> b(a), c(a);
    REP (i, a) {
        std::cin >> b[i] >> c[i];
    }
    std::cin >> d;
    auto ans = solve(a, b, c, d);
    std::cout << ans << '\n';
    return 0;
}
