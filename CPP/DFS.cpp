#include<bits/stdc++.h>
using ll = long long;
const ll N = 1e5 + 7;
std::vector<ll> arr[N]; // changed from arr to g[N] for adjacency list
std::vector<bool> vis(N, false);

void dfs(ll src) { // fixed parameter name to match usage
    vis[src] = true;
    for(ll v:arr[src]) {
        if(!vis[v]) {
            dfs(v);
        }
    }

}


void solve() {
    ll n, m; 
    std::cin >> n >> m;
    while (m--) {
        int u, v;
        std::cin >> u >> v;
        arr[u].push_back(v);
        arr[v].push_back(u); // remove for directed graph
    }
    ll src; 
    std::cin >> src;
    dfs(src);

    for (int i = 0; i < n; i++) { 
        for (ll v : arr[i]) {
            std::cout << v << ' ';
        }
        std::cout << "\n";
    }
}

int main() {
    std::ios::sync_with_stdio(false); // fixed typo: snyc → sync
    std::cin.tie(nullptr);
    
    solve();
}
