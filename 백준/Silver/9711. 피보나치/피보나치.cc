#include <iostream>
#define fio cin.tie(0)->sync_with_stdio(0)

using namespace std;

#include <vector>
int dp_pth_q(int P, int Q){
	vector<long long>fibo(P+1, 0);
	fibo[1] = 1; fibo[2] = 1;
	for(int i=3; i<=P; i++){
		fibo[i] = fibo[i-1] + fibo[i-2];
		fibo[i] %= Q;
	}
	return fibo[P]%Q; 
}
int main() {
	fio;
	int T; cin >> T;
	for(int tc=1; tc<= T; tc++){
		int P, Q; cin >> P >> Q;
		int ans = dp_pth_q(P, Q);
		cout <<"Case #"<< tc <<": "<< ans<<'\n';
	}

	return 0;
}