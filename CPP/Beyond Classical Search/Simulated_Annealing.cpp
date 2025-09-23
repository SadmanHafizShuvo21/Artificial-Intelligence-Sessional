#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define F first
#define S second
#define all(x) x.begin(),x.end()

double f(double x) {
    return -x*x + 5*x + 10; // Sample function
}

int main() {
    srand(time(0));
    double x = 0, lim = 1e3, lmin = 1e-6, alpha = 0.99;
    while(lim > lmin) {
        double nx = x + (rand()%2001 - 1000)/1000.0; // [-1,1] random step
        double dE = f(nx) - f(x);
        if(dE > 0 || exp(dE/lim) > (rand()%1001)/1000.0) {
            x = nx;
        }
        lim *= alpha;
    }
    cout << fixed << setprecision(6) << "Max at x = " << x << ", f(x) = " << f(x) << '\n';
}
