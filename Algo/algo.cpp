#include<iostream>
#include<vector>
#define MOD 1000000007
#define LL long long
#define MAX(X,Y) (X>Y?X:Y)
#define MIN(X,Y) (X<Y?X:Y)
using namespace std;
vector<LL> seq;
LL ans[10001][10001];
int main(){
    int n=10000;
    //cin>>n;
    seq.push_back(0);
    for(int i=1;i<n;i++)
        seq.push_back((seq[i-1]*seq[i-1]+45)%MOD);
    for(int i=0;i<n;i++)
        ans[i][i]=seq[i];
    for(int i=0;i+1<n;i++)
        ans[i][i+1]=MAX(seq[i],seq[i+1]);
    for(int l=3;l<=n;l++)
        for(int s=0;s+l-1<n;s++){
            int e=s+l-1;
            LL a1,a2;
            a1=seq[s]+MIN(ans[s+2][e],ans[s+1][e-1]);
            a2=seq[e]+MIN(ans[s+1][e-1],ans[s][e-2]);
            ans[s][e]=MAX(a1,a2);
        }
    cout<<ans[0][n-1]<<endl;
    return 0;
}
