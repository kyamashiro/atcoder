#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; (i) < (int)(n); ++ (i))
#define REP3(i, m, n) for (int i = (m); (i) < (int)(n); ++ (i))
#define REP_R(i, n) for (int i = (int)(n) - 1; (i) >= 0; -- (i))
#define REP3R(i, m, n) for (int i = (int)(n) - 1; (i) >= (int)(m); -- (i))
#define ALL(x) ::std::begin(x), ::std::end(x)
using namespace std;


auto solve(int n, const std::vector<int64_t> &a) {
    // TODO: edit here
}

// generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    // failed to analyze input format
    // TODO: edit here
    int n;
    std::cin >> n;
    std::vector<int64_t> a(n);
    REP (i, n) {
        std::cin >> a[i];
    }
    auto ans = solve(n, a);
    std::cout << a << '\n';
    REP (i, a) {
        std::cout << b[i] << '\n';
    }
    return 0;
}
