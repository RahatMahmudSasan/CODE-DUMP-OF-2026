#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    bool isPrime = (n >= 2);
    int i = 2;

    while (isPrime && i * i <= n) {
        if (n % i == 0) {
            isPrime = false;
        }
        i++;
    }

    if (isPrime) {
        cout << "Prime" << endl;
    }
    else {
        cout << "Not prime" << endl;
    }

    return 0;
}
