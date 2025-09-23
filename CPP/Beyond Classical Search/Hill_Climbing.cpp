#include <bits/stdc++.h>
using namespace std;

double f(double x) {
    return -x*x + 5*x + 10;
}

int main() {
    double x = 0, step = 0.01;
    int lim = 1000;

    for (int i = 0; i < lim; i++) {
        double left = f(x - step), right = f(x + step);

        if (right > f(x)) {
            x += step;   // move right
        }
        else if (left > f(x)) {
            x -= step; // move left
        }
        else {
            step *= 0.5;               // shrink step if stuck
        }
    }

    cout << fixed << setprecision(6) << "Max at x = " << x << ", f(x) = " << f(x) << "\n";
}
