#include<bits/stdc++.h>
using ll = long long;
const ll N = 1e5 + 7;
std::vector<std::pair<ll, ll>> arr[N];
std::vector<bool> vis(N, false);

ll ucs(ll src, ll goal) {
    std::priority_queue<std::pair<ll, ll>, std::vector<std::pair<ll, ll>>> pq;
    pq.push({0, src});
    while (!pq.empty()) {
        auto [cost, u] = pq.top(); 
        pq.pop();
        if (vis[u]) {
            continue;
        }
        vis[u] = true;
        if (u == goal) {
            return cost;
        }
        for (auto [v, w] : arr[u]) {
            if (!vis[v]) {
                pq.push({cost + w, v});
            }
        }
    }
    return -1;
}

void solve() {
    ll n, m; 
    std::cin >> n >> m;
    while (m--) {
        ll u, v, w;
        std::cin >> u >> v >> w;
        arr[u].emplace_back(v, w);
        // arr[v].emplace_back(u, w); // uncomment for undirected graph
    }
    ll src, goal; 
    std::cin >> src >> goal;
    std::cout << ucs(src, goal) << '\n';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    solve();
}
