#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;

constexpr int64_t MOD = 998244353;
int64_t solve(int64_t N, int M, int64_t K, int64_t S, int64_t T, int64_t X, const std::vector<int64_t> &U, const std::vector<int64_t> &V) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int64_t N;
    int M;
    int64_t K, S, T, X;
    std::cin >> N >> M;
    std::vector<int64_t> U(M), V(M);
    std::cin >> K >> S >> T >> X;
    REP (i, M) {
        std::cin >> U[i] >> V[i];
    }
    auto ans = solve(N, M, K, S, T, X, U, V);
    std::cout << ans << '\n';
    return 0;
}
