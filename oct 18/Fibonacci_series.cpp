#include <iostream>
using namespace std;

int main() {
    int n;
    int a = 0;
    int b = 1;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        if (i > 1) {
            cout << " ";
        }
        cout << a;
        int next = a + b;
        a = b;
        b = next;
    }
    cout << endl;

    return 0;
}
