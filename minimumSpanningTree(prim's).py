#include<cstring>
#include<iostream>
usingnamespacestd;
#defineINF9999999
#defineV5
intG[V][V]= {
{0,9,75,0,0},
{9,0,95,19,42},
{75,95,0,51,66},
{0,19,51,0,31},
{0,42,66,31,0}};
intmain()
{
intno_edge;
intselected[V];
memset(selected,false,sizeof(selected))
no_edge=0;
selected[0]=true;
intx;
inty;
cout<<"Edges"
<<":"
<<"Weight";
cout<<endl;
while(no_edge<V-1)
{
x=0;
y=0;
for(inti=0;i<V;i++)
{
if(selected[i])
{
for(intj=0;j<V;j++)
{
if(!selected[j]&&G[i][j])
{
if(min>G[i][j])
{
min=G[i][j];
x=i;
y=j;
}
}
}
}
}
cout<<x<<"_"<<y<<":"<<G[x][y];
cout<<endl;
selected[y]=true;
no_edge++;
}
return0;
}
