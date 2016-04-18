#include<cstdio>
using namespace std;

long long N,K;
int main()
{
	int T;
	scanf("%d",&T);
	while (T--)
	{
		scanf("%lld%lld",&N,&K);
		long long f1 = 0;
		long long f2;
		long long X;
		for (auto i = 2; i <= N; ++i)
		{
				if (f1 + K < i)//表示很有可能跳过X个i
				{
					X = (i - f1) / K;//能跳过多少个
					if (i + X < N)//如果没有跳过n，就是i<=N
					{
						i = i + X;//i直接到i+X
						f2 = (f1 + X*K);//由于f1+X*M肯定<=i,所以这里不用%i
						f1 = f2;
					}
					else//如果跳过了n,那么就不能直接加X了，而是只需要加(N-i)个M即可
					{
						f2 = f1+(N-i)*K;
						f1 = f2;
						i = N;
					}
				}
				f2 = (f1 + K) % i;//如果f1+M>=i或者跳过上面的一些i之后还是要继续当前i对于的出列的人
				f1 = f2;
		}
		printf("%lld\n",f2);
	}
	return 0;
}