#include<bits/stdc++.h>
using ll = long long;
const ll N = 1e5 + 7;
std::vector<ll> arr[N];
std::vector<bool> vis(N, false);
std::vector<ll> res;

void bfs(ll src) {
    std::queue<ll> q;
    vis[src] = true;
    q.push(src);
    res.push_back(src);
    while (!q.empty()) {
        ll u = q.front(); 
        q.pop();
        for (ll v : arr[u]) {
            if (!vis[v]) {
                vis[v] = true;
                q.push(v);
                res.push_back(v);
            }
        }
    }
}

void solve() {
    ll n, m; std::cin >> n >> m;
    while (m--) {
        ll u, v;
        std::cin >> u >> v;
        arr[u].push_back(v);
        arr[v].push_back(u); // remove for directed graph
    }
    ll src; 
    std::cin >> src;
    bfs(src);
    // for (int i = 0; i < n; i++) { 
    //     for (ll v : arr[i]) {
    //         std::cout << v << ' ';
    //     }
    //     std::cout << "\n";
    // }
    for (int i = 0; i < n; i++) {
        std::cout << res[i] << " \n"[i == n - 1];
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    solve();
}
