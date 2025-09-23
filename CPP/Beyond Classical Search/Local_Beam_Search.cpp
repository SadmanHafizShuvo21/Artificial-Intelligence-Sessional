#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define F first
#define S second
#define all(x) x.begin(),x.end()

double f(double x) {
    return -x*x + 5*x + 10;
}

int main() {
    int k = 3, steps = 100;
    vector<double> beam(k);
    for(auto &x : beam) x = (rand()%2001 - 1000)/1000.0; // init [-1,1]

    while(steps--) {
        vector<pair<double,double>> next;
        for(auto x : beam) {
            for(int d=-1; d<=1; d++) {
                double nx = x + d*0.1;
                next.push_back({f(nx), nx});
            }
        }
        sort(all(next), greater<>());
        for(int i=0; i<k; i++) beam[i] = next[i].S;
    }

    double best = beam[0];
    for(auto x : beam) if(f(x) > f(best)) best = x;
    cout << fixed << setprecision(6) << "Max at x = " << best << ", f(x) = " << f(best) << '\n';
}
