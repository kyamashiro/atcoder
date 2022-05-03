#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


std::vector<auto> solve(int64_t N, int K, int L, const std::vector<int64_t> &p, const std::vector<int64_t> &q, const std::vector<int64_t> &r, const std::vector<int64_t> &s) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int64_t N;
    int K, L;
    std::cin >> N >> K;
    std::vector<int64_t> p(K), q(K);
    std::cin >> L;
    std::vector<int64_t> r(L), s(L);
    REP (i, K) {
        std::cin >> p[i] >> q[i];
    }
    REP (i, L) {
        std::cin >> r[i] >> s[i];
    }
    auto ans = solve(N, K, L, p, q, r, s);
    REP (i, (int)ans.size()) {
        std::cout << ans[i] << ' ';
    }
    std::cout << '\n';
    return 0;
}