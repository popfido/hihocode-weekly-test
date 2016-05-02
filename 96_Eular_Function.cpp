#include <iostream>
#include <cstring>

using namespace std;

long long l, r;
bool isPrime[5000001];
long long primeList[5000001];
long long phi[5000001];
long long primeCount = 0;

int main(){
    cin >> l >> r;
    memset(isPrime, true, sizeof(isPrime));
    phi[1] = 1;

    for (long long i=2; i<=r; i++){
        if (isPrime[i]){
            primeList[++primeCount] = i;
            phi[i] = i-1;
        }
        long long j=1;
        while(i*primeList[j] <= r){
            isPrime[i*primeList[j]] = false;
            if (i % primeList[j] == 0) {
                phi[i * primeList[j]] = phi[i] * primeList[j];
                break;
            }
            else
                phi[i * primeList[j]] = phi[i] * (primeList[j] - 1);
            j++;
        }
    }

    long long min = phi[l];
    long long argmin = l;
    for (long long i=l+1; i<=r; i++)
        if (phi[i] < min ){
            min = phi[i];
            argmin = i;
        }
    cout << argmin;
    return 0;
}