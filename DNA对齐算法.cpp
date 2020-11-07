#include<stdio.h>

#define max 10
#define row 10
#define col 8

int OPT[11][9];

char x[11] = {'A','G','C','T','G','T','C','A','A','G',' '};
char y[9] = {'T','A','C','G','G','T','A','G',' '};

int getOPT(int i, int j );
int Min(int a,int b,int c);
//分置算法 
int main(){
	printf("%d\n",getOPT(0,0));
	return 0;
} 
int getOPT(int i, int j ){

	int opt,penalty; 

    if (i == row) 
		return opt = 2*(col-j);

    else if (j == col) 
		return opt = 2*(row-i);

    else{
	    if (x[i] == y[j])
			penalty = 0;
 	    else 
			penalty = 1;
    }
 	return opt= Min(getOPT(i+1, j+1)+penalty,getOPT(i+1, j)+2, getOPT(i, j+1)+2);

}

/* 
//动态规划算法 
int main(){

	int i,j,k;

	for(k=max;k>1;k--){
		//求行的值 
	    for(i=k;i>=0;i--)
			OPT[i][k-2] = getOPT(i,k-2);

		//求列的值  
	    for(j=k-3;j>=0;j--)
		    OPT[k][j] = getOPT(k,j);
	}

	printf("%d\n",OPT[0][0]);
	return 0;

} 

int getOPT(int i, int j ){

	int opt,penalty; 

    if (i == row) 
		return opt = 2*(col-j);

    else if (j == col) 
		return opt = 2*(row-i);

    else{
	    if (x[i] == y[j])
			penalty = 0;
 	    else 
			penalty = 1;
    }
 	return opt= Min(OPT[i+1][j+1]+penalty, OPT[i+1][j]+2, OPT[i][j+1]+2);

}
*/ 
int Min(int a,int b,int c)
{	
	int temp;
	if(a>b) 
		temp=b;
	else
		temp=a;

	if(temp>c)
		return c;
	else
		return temp;
}





