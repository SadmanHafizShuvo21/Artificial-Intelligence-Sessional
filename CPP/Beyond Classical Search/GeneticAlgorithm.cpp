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
    int pop = 10, gen = 100;
    vector<double> P(pop);
    for(auto &x : P) x = (rand()%2001 - 1000)/1000.0; // init [-1,1]

    while(gen--) {
        vector<pair<double,double>> fit;
        for(auto x : P) fit.push_back({f(x), x});
        sort(all(fit), greater<>());

        vector<double> next;
        for(int i=0; i<pop/2; i++) {
            double p1 = fit[i].S, p2 = fit[(i+1)%pop].S;
            double child = (p1 + p2)/2 + ((rand()%201 - 100)/1000.0); // crossover + mutation
            next.push_back(child);
            next.push_back(p1); // elitism
        }
        P = next;
    }

    double best = *max_element(all(P), [](double a, double b){ return f(a) < f(b); });
    cout << fixed << setprecision(6) << "Max at x = " << best << ", f(x) = " << f(best) << '\n';
}
