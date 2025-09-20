#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll N = 1e5 + 7;

vector<pair<ll,ll>> arr[N]; // {neighbor, weight}
vector<ll> dist(N, LLONG_MAX), parent(N, -1);

void dijkstra(ll start, ll n) {
    dist.assign(n, LLONG_MAX);
    parent.assign(n, -1);
    dist[start] = 0;

    priority_queue<pair<ll,ll>, vector<pair<ll,ll>>, greater<>> pq;
    pq.push({0, start});

    while(!pq.empty()) {
        auto [d, u] = pq.top(); 
        pq.pop();
        if(d > dist[u]) continue;

        for(auto [v, w] : arr[u]) {
            if(dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                parent[v] = u;
                pq.push({dist[v], v});
            }
        }
    }
}

void solve() {
    ll n, e;
    cin >> n >> e;

    for(ll i = 0; i < n; i++) arr[i].clear();

    for(ll i = 0; i < e; i++) {
        ll u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        arr[u].push_back({v, w});
        arr[v].push_back({u, w});
    }

    ll start, goal;
    cin >> start >> goal;
    start--, goal--;

    dijkstra(start, n);

    if(dist[goal] == LLONG_MAX) {
        cout << "No path found\n";
        return;
    }

    vector<ll> path;
    for(ll v = goal; v != -1; v = parent[v]) path.push_back(v);
    reverse(path.begin(), path.end());

    cout << "Shortest path from " << start + 1 << " to " << goal + 1 << " (weight " << dist[goal] << "): ";
    for(size_t i = 0; i < path.size(); i++) {
        cout << path[i] + 1 << " \n"[i == path.size() - 1];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}
