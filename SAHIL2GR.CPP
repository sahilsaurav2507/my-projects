#include<iostream>
using namespace std;
int main()
{

  int marks;
  cout<<"Enter your marks :";
  cin>>marks;
int a;
    if(a<0 && a>100)
    {
       cout<<"invalid number"<<endl;
    }
    else if(marks<=100 && marks>=90)
    {
       cout<<"grade A"<<endl;
    }
else if(marks<=90 && marks>80)
{
   cout<<"grade B"<<endl;
}

else if(marks<=80 && marks>70)
{
    cout<<"grade C"<<endl;
}
else if(marks<=70 && marks>=60)
{
    cout<<"grade D"<<endl;
}
else if(marks<=60 && marks>=40)
{  
    cout<<"grade E"<<endl;
}
else
{
    cout<<"Fail"<<endl;
}

return 0;
}