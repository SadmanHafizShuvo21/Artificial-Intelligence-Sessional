#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define F first
#define S second
#define all(x) x.begin(),x.end()

double f(double x) {
    return -x*x + 5*x + 10; // Example function
}

int main() {
    double x = 0, step = 0.01, lim = 1000;
    for(int i=0; i<lim; i++) {
        double nx = x + step;
        if(f(nx) > f(x)) {
            x = nx;
        }
        else {
            step *= -0.5; // reverse & shrink step
        }
    }
    cout << fixed << setprecision(6) << "Max at x = " << x << ", f(x) = " << f(x) << '\n';
}
