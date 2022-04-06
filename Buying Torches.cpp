#include <iostream>
using namespace std;

int64_t ceil_div(int64_t a, int64_t b) {
    return (a + b - 1) / b;
}
void run_case(){
    int64_t X, Y, K;
    cin >> X >> Y >> K;
    int64_t trades = ceil_div(K * Y + K - 1, X - 1);
    trades += K;
    cout << trades << '\n';
}

int main()
{
    int tests;
    cin >> tests;
 
    while (tests-- > 0)
        run_case();
}