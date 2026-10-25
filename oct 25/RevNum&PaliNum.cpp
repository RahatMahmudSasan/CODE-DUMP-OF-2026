#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int rev = 0;
    int temp = n;

    while (temp > 0) {
        int digit = temp % 10;
        rev = rev * 10 + digit;
        temp = temp / 10;
    }

    cout << "Reversed: " << rev << endl;

    if (rev == n) {
        cout << "Palindrome: Yes" << endl;
    } else {
        cout << "Palindrome: No" << endl;
    }

    return 0;
}