#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


auto solve(int n, int64_t k, const std::vector<std::string> &a) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    int64_t k;
    std::cin >> n;
    std::vector<std::string> a(n);
    std::cin >> k;
    REP (i, n) {
        std::cin >> a[i];
    }
    auto ans = solve(n, k, a);
    REP (i, n) {
        std::cout << d[i] << '\n';
    }
    std::cout << e << '\n';
    return 0;
}
