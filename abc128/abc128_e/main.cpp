#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


auto solve(int N, int Q, const std::vector<int64_t> &S, const std::vector<int64_t> &T, const std::vector<int64_t> &X, const std::vector<int64_t> &D) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int N, Q;
    std::cin >> N;
    std::vector<int64_t> S(N), T(N), X(N);
    std::cin >> Q;
    std::vector<int64_t> D(Q);
    REP (i, N) {
        std::cin >> S[i] >> T[i] >> X[i];
    }
    REP (i, Q) {
        std::cin >> D[i];
    }
    auto ans = solve(N, Q, S, T, X, D);
    REP (i, N) {
        std::cout << a[i] << '\n';
    }
    REP (i, N) {
        std::cout << d[i] << '\n';
    }
    return 0;
}
