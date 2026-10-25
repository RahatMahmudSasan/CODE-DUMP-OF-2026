#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    long long result = 1;
    /*
    int i = 1;
    if (n >= 1) {
        do {
            result *= i;
            i++;
        } while (i <= n);
    }*/
    for (int i = 2; i <= n; i++) {
    result *= i;
    }

    cout << result << endl;

    return 0;
}
