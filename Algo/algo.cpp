#include<iostream>
#include<vector>
#define MOD 1000000007
#define LL long long
#define MAX(X,Y) (X>Y?X:Y)
#define MIN(X,Y) (X<Y?X:Y)
using namespace std;
vector<LL> seq;
int main(){
    int n=100000000;
    //cin>>n;
    //generate sequence
    seq.push_back(0);
    for(int i=1;i<n;i++)
        seq.push_back(((seq[i-1]*seq[i-1])%MOD+45)%MOD);

    //simulate game
    LL score=0;
    int s=0;
    int e=n-1;
    while(s<=e){
    	if(seq[s]>=seq[e]){
		score+=seq[s];
		s++;
	}
	else{
		score+=seq[e];
		e--;
	}
	if(s<=e){
		if(seq[s]>=seq[e])
			s++;
		else
		        e--;
	}
	if(score<0)
		cout<<score<<endl;
    }
    cout<<"F(100000000) : "<<score<<endl;
    return 0;
}
