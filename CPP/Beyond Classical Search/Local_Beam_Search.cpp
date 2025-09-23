#include <bits/stdc++.h>
using namespace std;

double f(double x) {
    return -x*x + 5*x + 10;
}

int main() {
    int k = 10, steps = 100;
    vector<double> beam(k);

    // Random initialization in [-1,1]
    for (auto &x : beam) 
        x = (rand() % 2001 - 1000) / 1000.0;

    while (steps--) {
        vector<pair<double,double>> next;
        for (auto x : beam) {
            for (int d = -1; d <= 1; d++) {
                double nx = x + d*0.1;
                next.push_back({f(nx), nx});
            }
        }
        sort(next.rbegin(), next.rend()); // descending order
        for (int i = 0; i < k; i++) 
            beam[i] = next[i].second;
    }

    // Find the best x
    double best = *max_element(beam.begin(), beam.end(), [](double a, double b){ return f(a) < f(b); });
    cout << fixed << setprecision(6) << "Max at x = " << best << ", f(x) = " << f(best) << '\n';
}
