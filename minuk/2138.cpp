#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int N;
    vector<int> ary, target;
    string s1, s2;
    cin >> N >> s1 >> s2;
    ary.resize(N);
    target.resize(N);
    for (int i = 0; i < N; ++i) {
        ary[i] = (int)(s1[i] - '0');
        target[i] = (int)(s2[i] - '0');
    }
    
    vector<int> ary2(ary);
    int cnt1 = 1, cnt2 = 0;
    ary[0] ^= 1;
    ary[1] ^= 1;
    for (int i = 0; i < N - 1; ++i) {
        if (ary[i] != target[i]) {
            ++cnt1;
            ary[i] ^= 1;
            ary[i + 1] ^= 1;
            if (i < N - 2) ary[i + 2] ^= 1;
        }
    }
    for (int i = 0; i < N - 1; ++i) {
        if (ary2[i] != target[i]) {
            ++cnt2;
            ary2[i] ^= 1;
            ary2[i + 1] ^= 1;
            if (i < N - 2) ary2[i + 2] ^= 1;
        }
    }
    if (ary[N - 1] != target[N - 1]) cnt1 = (int)1e9;
    if (ary2[N - 1] != target[N - 1]) cnt2 = (int)1e9;
    int res = min(cnt1, cnt2);
    if (res == (int)1e9) res = -1;
    cout << res;
    return 0;
}