#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define F first
#define S second

vector<int>g[105];
int h[105], vis[105];

void bfs(int s, int t){
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<>>q;
    q.push({h[s],s});
    while(q.size()){
        auto [_,u]=q.top(); 
        q.pop();
        if(vis[u]) {
            continue;
        }
        cout<< u <<" ";
        if(u == t){
            cout<<"\nGoal!\n"; 
            return;
        }
        vis[u]=1;
        for(int v:g[u]) {
            if(!vis[v]) {
                q.push({h[v],v});
            }
        }
    }
}

int main(){
    int n, m; 
    cin >> n >> m;
    while(m--) {
        int u,v; 
        cin>>u>>v;
        g[u].pb(v);
    }
    for(int i=1; i<= n; i++) {
        cin >> h[i];
    }
    int s,t; 
    cin >> s >> t;
    bfs(s,t);
}
