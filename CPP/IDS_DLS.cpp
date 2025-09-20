#include<bits/stdc++.h>
using namespace std;
using ll = long long;
const ll N = 1e5 + 7;

vector<pair<ll,ll>> arr[N]; // weights ignored for IDS when w = 1
vector<ll> path;
bool found = false;

bool dls(ll u, ll goal, ll limit){
    path.push_back(u);
    if(u == goal){
        found = true;
        return true;
    }
    if(limit == 0){
        path.pop_back();
        return false;
    }
    for(auto [v, w] : arr[u]){
        if(find(path.begin(), path.end(), v) == path.end()){
            if(dls(v, goal, limit - 1)) {
                return true;
            }
        }
    }
    path.pop_back();
    return false;
}

bool ids(ll start, ll goal, ll max_depth){
    for(ll depth = 0; depth <= max_depth; depth++){
        path.clear();
        found = false;
        if(dls(start, goal, depth)) return true;
    }
    return false;
}

void solve(){
    ll n, e;
    cin >> n >> e;
    for(ll i = 0; i < e; i++){
        ll u, v, w;
        cin >> u >> v >> w;
        u--, v--;
        arr[u].push_back({v, w});
        arr[v].push_back({u, w});
    }

    ll start, goal, max_depth;
    cin >> start >> goal >> max_depth;
    start--, goal--;

    if(ids(start, goal, max_depth)){
        cout << "IDS path from " << start+1 << " to " << goal+1 << ": ";
        for (int i = 0; i < path.size(); i++) {
            std::cout << path[i] + 1 << " \n"[i == path.size() - 1];
        }
    } 
    else {
        cout << "No path found within depth " << max_depth << "\n";
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
}
