#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll N = 1e5 + 7;
vector<pair<ll,ll>> adj[N]; // {neighbor, weight}
vector<ll> parent(N, -1);

// A* search from start to goal using heuristic h[]
vector<ll> a_star(ll start, ll goal, ll n, vector<ll>& h) {
    vector<ll> g(n, LLONG_MAX); // cost from start to node
    g[start] = 0;

    priority_queue<pair<ll,ll>, vector<pair<ll,ll>>, greater<>> pq;
    pq.push({h[start], start});

    while(!pq.empty()) {
        auto [f, u] = pq.top(); 
        pq.pop();

        if(u == goal) {
            break;
        }

        for(auto [v, w] : adj[u]) {
            if(g[v] > g[u] + w) {
                g[v] = g[u] + w;
                parent[v] = u;
                pq.push({g[v] + h[v], v});
            }
        }
    }

    if(g[goal] == LLONG_MAX) return {}; // no path

    vector<ll> path;
    for(ll v = goal; v != -1; v = parent[v]) path.push_back(v);
    reverse(path.begin(), path.end());
    return path;
}

void solve() {
    ll n, e;
    cin >> n >> e;

    for(ll i = 0; i < n; i++) {
        adj[i].clear();
    }

    while (e--) {
        ll u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w}); // remove if directed
    }

    ll start, goal;
    cin >> start >> goal;
    start--, goal--;

    vector<ll> h(n, 0); // heuristic array
    for(ll i = 0; i < n; i++) {
        cin >> h[i]; // optional: input heuristics
    }

    vector<ll> path = a_star(start, goal, n, h);
    if(path.empty()) {
        cout << "No path found\n";
        return;
    }

    ll total_cost = 0;
    for(int i = 1; i < path.size(); i++) {
        ll u = path[i - 1]; 
        ll v = path[i];
        for(auto [to, w] : adj[u]) {
            if(to == v) { 
                total_cost += w; 
                break; 
            }
        }
    }

    cout << "A* path from " << start + 1 << " to " << goal + 1 << " (weight " << total_cost << "): ";
    for(int i = 0; i < path.size(); i++)
        cout << path[i] + 1 << " \n"[i == path.size() - 1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}

// #include <bits/stdc++.h>
// using namespace std;
// using ll = long long;

// const ll N = 1e5 + 7;
// vector<pair<ll,ll>> adj[N]; 
// vector<ll> parent(N, -1);

// vector<ll> a_star(ll start, ll goal, ll n, vector<ll>& h) {
//     vector<ll> g(n, LLONG_MAX);
//     g[start] = 0;

//     priority_queue<pair<ll,ll>, vector<pair<ll,ll>>, greater<>> pq;
//     pq.push({h[start], start});

//     while(!pq.empty()) {
//         auto [f, u] = pq.top(); 
//         pq.pop();

//         if(u == goal) break;

//         for(auto [v, w] : adj[u]) {
//             if(g[v] > g[u] + w) {
//                 g[v] = g[u] + w;
//                 parent[v] = u;
//                 pq.push({g[v] + h[v], v});
//             }
//         }
//     }

//     if(g[goal] == LLONG_MAX) return {};

//     vector<ll> path;
//     for(ll v = goal; v != -1; v = parent[v]) path.push_back(v);
//     reverse(path.begin(), path.end());
//     return path;
// }

// void solve() {
//     ll n, e;
//     cin >> n >> e;

//     for(ll i = 0; i < n; i++) adj[i].clear();

//     while (e--) {
//         ll u, v, w;
//         cin >> u >> v >> w;
//         u--, v--;
//         adj[u].push_back({v, w});
//         adj[v].push_back({u, w});
//     }

//     ll start, goal;
//     cin >> start >> goal;
//     start--, goal--;

//     vector<ll> h(n, 0);
//     for(ll i = 0; i < n; i++) cin >> h[i];

//     vector<ll> path = a_star(start, goal, n, h);
//     if(path.empty()) {
//         cout << "No path\n";
//         return;
//     }

//     for(int i = 0; i < path.size(); i++)
//         cout << path[i] + 1 << " \n"[i == path.size() - 1];
// }

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);
//     solve();
// }

