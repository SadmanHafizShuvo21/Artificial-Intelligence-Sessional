#include<bits/stdc++.h>
using ll = long long;
const ll N = 1e5 + 7;
const ll inf = 1e18;
std::vector<std::pair<ll, ll>> arr[N];
std::vector<bool> vis(N, false);

ll ucs(ll src, ll goal, std::vector<ll> &path, ll n) {
    std::priority_queue<std::pair<ll, ll>, std::vector<std::pair<ll, ll>>, std::greater<>> pq;
    std::vector<ll> parent(n, -1), dist(n, inf);

    dist[src] = 0;
    pq.push({0, src});

    while (!pq.empty()) {
        auto [cost, u] = pq.top();
        pq.pop();
        if (vis[u]) continue;
        vis[u] = true;

        if (u == goal) {
            path.clear();
            for (ll v = goal; v != -1; v = parent[v]) {
                path.push_back(v);
            }
            std::reverse(path.begin(), path.end());
            return cost;
        }

        for (auto [v, w] : arr[u]) {
            if (dist[v] > cost + w) {
                dist[v] = cost + w;
                parent[v] = u;   // ✅ update parent on better path
                pq.push({dist[v], v});
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
    std::vector<ll> path;
    ll cost = ucs(src, goal, path, n);
    std::cout << cost << '\n';
    for (int i = 0; i < path.size(); i++)
        std::cout << path[i] << " \n"[i == path.size() - 1];
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    solve();
}

// #include<bits/stdc++.h>
// using ll = long long;
// const ll N = 1e5 + 7;
// std::vector<std::pair<ll, ll>> arr[N];
// std::vector<bool> vis(N, false);

// ll ucs(ll src, ll goal) {
//     std::priority_queue<std::pair<ll, ll>, std::vector<std::pair<ll, ll>>> pq;
//     pq.push({0, src});
//     while (!pq.empty()) {
//         auto [cost, u] = pq.top(); 
//         pq.pop();
//         if (vis[u]) {
//             continue;
//         }
//         vis[u] = true;
//         if (u == goal) {
//             return cost;
//         }
//         for (auto [v, w] : arr[u]) {
//             if (!vis[v]) {
//                 pq.push({cost + w, v});
//             }
//         }
//     }
//     return -1;
// }

// void solve() {
//     ll n, m; 
//     std::cin >> n >> m;
//     while (m--) {
//         ll u, v, w;
//         std::cin >> u >> v >> w;
//         arr[u].emplace_back(v, w);
//         // arr[v].emplace_back(u, w); // uncomment for undirected graph
//     }
//     ll src, goal; 
//     std::cin >> src >> goal;
//     std::cout << ucs(src, goal) << '\n';
// }

// int main() {
//     std::ios::sync_with_stdio(false);
//     std::cin.tie(nullptr);
//     solve();
// }