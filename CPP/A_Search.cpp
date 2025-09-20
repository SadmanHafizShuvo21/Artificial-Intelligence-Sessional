#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define F first
#define S second

vector<pair<int,int>> g[105]; 
int h[105], gval[105], vis[105];

void astar(int s, int t){
    for(int i = 0; i < 105; i++) gval[i] = INT_MAX;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> q;
    gval[s] = 0;
    q.push({h[s], s});
    while(q.size()){
        int u = q.top().S; q.pop();
        if(vis[u]) continue;
        cout << u << " ";
        if(u == t){ cout << "\nGoal!\n"; return; }
        vis[u] = 1;
        for(auto [v, c] : g[u]){
            int new_g = gval[u] + c;
            if(new_g < gval[v]){
                gval[v] = new_g;
                q.push({gval[v] + h[v], v});
            }
        }
    }
}

int main(){
    int n, m; cin >> n >> m;
    while(m--){
        int u, v, c; cin >> u >> v >> c;
        g[u].pb({v, c});
    }
    for(int i = 1; i <= n; i++) cin >> h[i];
    int s, t; cin >> s >> t;
    astar(s, t);
}
