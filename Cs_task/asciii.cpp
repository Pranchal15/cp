#include<iostream>
using namespace std;
int main()
{
    int t,x,y;
    char str1[1000];
    
    cin>>t;
    while(t--)

    {
      

        cin >> x;
        cin >> str1;
        
        for(int i=0;i<x;i++)
        {
             cout<< (int)(str1[i]);
        }
         
       cout << "\n";
        


    }

    
}