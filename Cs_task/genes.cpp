#include<iostream>
using namespace std;
int main()
{
    int t,l;
    cin >> t;
    char str1[1000],str2[1000],str3[2000];
    while(t--)
    {
        cin >>l;
        cin>>str1;
        cin >> str2;
        int j=0;
        for (int i=0;i<l;i++,j++)
        {
            str3[j]= str1[i];
            j++;
            str3[j]=str2[i];
            
        }
        for (int i=0;i<2*l;i++)
        {
            cout << str3[i];
        }
        

    }
}