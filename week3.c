#include <iostream>
#include <string>

using namespace std;

void buildNext(string pat, int *nextval)
{
	int i = 0, j = -1;
	nextval[0] = -1;
	while(i != pat.size())
	{
		if(j == -1 || pat[i] == pat[j])
			nextval[++i] = ++j;
		else
			j = nextval[j];
	}
}

int kmp(string pat, int *next, string ori)
{
	int p = 0, q = 0, ret = 0;
	while(p != ori.size() && q != pat.size()){
		if(ori[p] == pat[q] || q == -1)
				p++, q++;
		else
			q = next[q];
		if(q == pat.size()){
			q = next[q];
			ret++;
		}
	}
	return ret;
}

int main()
{
	int N,i,j;
	cin >> N;
	string pat, ori;
	int ans;
	int next[10010];
	for(i=0;i<N;i++){
		cin >> pat >> ori;
		buildNext(pat, next);
		ans = kmp(pat, next, ori);
		cout << ans << endl;
	}

	return 0;
}
