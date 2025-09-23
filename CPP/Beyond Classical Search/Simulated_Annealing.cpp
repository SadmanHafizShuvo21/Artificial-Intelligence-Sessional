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
    double x = 0, T = 1e3, Tmin = 1e-6, alpha = 0.99;
    while(T > Tmin) {
        double nx = x + (rand()%2001 - 1000)/1000.0; // [-1,1] random step
        double dE = f(nx) - f(x);
        if(dE > 0 || exp(dE/T) > (rand()%1001)/1000.0) {
            x = nx;
        }
        T *= alpha;
    }
    cout << fixed << setprecision(6) << "Max at x = " << x << ", f(x) = " << f(x) << '\n';
}
