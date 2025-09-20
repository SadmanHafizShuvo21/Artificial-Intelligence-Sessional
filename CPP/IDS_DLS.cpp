#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll N = 1e5 + 7;

vector<pair<ll,ll>> arr[N];
vector<ll> path;
vector<int> vis;

bool dls(ll u, ll goal, ll limit) {
    path.push_back(u);
    vis[u] = 1;

    if (u == goal) {
        return true;
    }

    if (limit == 0) {
        path.pop_back();
        vis[u] = 0;
        return false;
    }

    for (auto [v, w] : arr[u]) {
        if (!vis[v]) {
            if (dls(v, goal, limit - 1)) {
                return true;
            }
        }
    }

    path.pop_back();
    vis[u] = 0;
    return false;
}

bool ids(ll start, ll goal, ll max_depth, ll n) {
    for (ll depth = 0; depth <= max_depth; depth++) {
        path.clear();
        vis.assign(n, 0);
        if (dls(start, goal, depth)) {
            return true;
        }
    }
    return false;
}

void solve() {
    ll n, e;
    cin >> n >> e;

    for (ll i = 0; i < n; i++) arr[i].clear(); // clear graph before use

    for (ll i = 0; i < e; i++) {
        ll u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        arr[u].push_back({v, w});
        arr[v].push_back({u, w});
    }

    ll start, goal, max_depth;
    cin >> start >> goal >> max_depth;
    start--, goal--;

    if (ids(start, goal, max_depth, n)) {
        cout << "IDS path from " << start + 1 << " to " << goal + 1 << ": ";
        for (int i = 0; i < path.size(); i++) {
            cout << path[i] + 1 << " \n"[i == path.size() - 1];
        }
    } 
    else {
        cout << "No path found within depth " << max_depth << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}
