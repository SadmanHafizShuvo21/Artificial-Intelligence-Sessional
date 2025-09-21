#include <bits/stdc++.h>
using ll = long long;
const ll N = 1e5 + 7;

std::vector<ll> arr[N], res;
std::vector<bool> vis(N, false);

void dfs(ll src) {
    vis[src] = true;
    res.push_back(src);
    for(ll v : arr[src]) {
        if(!vis[v]) {
            dfs(v);
        }
    }
}

void solve() {
    ll n, m;
    std::cin >> n >> m;

    // clear previous graph
    for(ll i = 0; i < n; i++) {
        arr[i].clear();
        vis[i] = false;
    }
    res.clear();

    for(ll i = 0; i < m; i++) {
        ll u, v;
        std::cin >> u >> v;
        u--; 
        v--; // convert to 0-based if input is 1-based
        arr[u].push_back(v);
        arr[v].push_back(u); // remove for directed graph
    }

    ll src;
    std::cin >> src;
    src--; // convert to 0-based if needed
    dfs(src);

    for(int i = 0; i < res.size(); i++)
        std::cout << res[i] + 1 << " \n"[i == res.size() - 1];
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    solve();
}
