#include<bits/stdc++.h>
using namespace std;
#define pb push_back
using ll = long long;
const ll N = 1e5 + 7;
vector<ll> g[N], path; // unweighted graph

bool dls(ll u, ll goal, ll limit){
    path.pb(u);
    if(u == goal){ 
        return true; 
    }

    if(limit == 0){ 
        path.pop_back(); 
        return false; 
    }

    for(ll v : g[u]){
        if(find(path.begin(), path.end(), v) == path.end()){
            if(dls(v, goal, limit - 1)) {
                return true;
            }
        }
    }
    path.pop_back();
    return false;
}

void solve() {
    ll n, e; 
    cin >> n >> e;
    while(e--){
        ll u, v; 
        cin >> u >> v;
        u--;
        v--;
        g[u].pb(v);
        g[v].pb(u);
    }

    ll s, t, d; 
    cin >> s >> t >> d;
    s--;
    t--;
    if(dls(s, t, d)){
        cout << "DLS path from " << s+1 << " to " << t+1 << ": ";
        for(ll i = 0; i < path.size(); i++) {
            cout << path[i] + 1 << " \n"[i == path.size() - 1];
        }
    } 
    else {
        cout << "No path found within depth " << d << "\n";
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
}
