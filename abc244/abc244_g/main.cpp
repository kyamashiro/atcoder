#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


std::vector<auto> solve(int64_t N, int M, const std::vector<int64_t> &u, const std::vector<int64_t> &v, std::string S) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int64_t N;
    int M;
    std::string S;
    std::cin >> N >> M;
    std::vector<int64_t> u(M), v(M);
    REP (i, M) {
        std::cin >> u[i] >> v[i];
    }
    std::cin >> S;
    auto ans = solve(N, M, u, v, S);
    std::cout << (int)ans.size() << '\n';
    REP (i, (int)ans.size()) {
        std::cout << A[i] << ' ';
    }
    std::cout << '\n';
    return 0;
}
