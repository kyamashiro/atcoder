#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;

const std::string YES = "YES";
const std::string NO = "NO";
bool solve(int N, const std::vector<int64_t> &a, const std::vector<int64_t> &b, const std::vector<int64_t> &c, const std::vector<int64_t> &d) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int N;
    std::cin >> N;
    std::vector<int64_t> a(N - 1), b(N - 1), c(N - 1), d(N - 1);
    REP (i, N - 1) {
        std::cin >> a[i] >> b[i];
    }
    REP (i, N - 1) {
        std::cin >> c[i] >> d[i];
    }
    auto ans = solve(N, a, b, c, d);
    std::cout << (ans ? YES : NO) << '\n';
    return 0;
}
