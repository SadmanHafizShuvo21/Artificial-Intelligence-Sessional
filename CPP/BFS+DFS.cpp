#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const ll N = 1e5 + 7;
std::vector<ll> arr[N];
std::vector<ll> res, res1;
std::vector<bool> vis(N, false);

void dfs (int n) {
    res.push_back(n);
    vis[n] = true;
    for (auto v : arr[n]) {
        if (!vis[v]) {
            dfs(v);
        }
    }
}

void bfs (int n) {
    queue<ll> q;
    vis[n] = true;
    q.push(n);
    while(!q.empty()) {
        ll u = q.front();
        q.pop();
        res1.push_back(u);
        for(auto v : arr[u]) {
            if (!vis[v]) {
                vis[v] = true;
                q.push(v);
            }
        }
    }
}

void solve() {
    ll n, e;
    std::cin >> n >> e;
    for (int i = 0; i < e; i++) {
        ll u, v;
        std::cin >> u >> v;
        u--;
        v--;
        arr[u].push_back(v);
        arr[v].push_back(u);
    }
    dfs(0);
    fill(vis.begin(), vis.begin() + n, false); // reset visited
    bfs(0);
    
    for (int i = 0; i < res.size(); i++) {
        std::cout << res[i] + 1 << " \n"[i + 1 == res.size()];
    }
    
    for (int i = 0; i < res1.size(); i++) {
        std::cout << res1[i] + 1 << " \n"[i + 1 == res1.size()];
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    solve();
}
