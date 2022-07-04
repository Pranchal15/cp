// #include<iostream>
// using namespace std;
// int main()
// {
//     int t,x,y;
//     char str1[1000],str2[1000];
//     int arr1[100]={0},arr2[100]={0};
//     cin>>t;
//     while(t--)

//     {
//         cin >> x>>y;
//         cin >> str1;
//         cin >> str2;
//         int flag=0;
//         for(int i=0;i<x;i++)
//         {
//              arr1[(int)(str1[i])]+=1;
//         }
//           for(int i=0;i<y;i++)
//         {
//              arr2[(int)(str2[i])]+=1;
//         }
// for (int k=65;k<=91;k++)
//         {
//             cout << arr1[k]<< " "<<arr2[k];
//             cout << "\n";
//         }
        
//         for (int k=65;k<=91;k++)
//         {
//             if(arr1[k]>arr2[k])
//             {
//                 flag=1;
//             }
//             if (flag==1){
//                 cout<<"NO\n";
//                 break;
//             }
//         }
//         if(flag==0){
//         cout << "YES"<<endl;}


//     }

    
// }
#include<iostream>
using namespace std;
int main()
{
    int t,x,y;
    char str1[1000],str2[1000];
    
    cin>>t;
    while(t--)

    {
        int arr1[200]={0},arr2[200]={0};

        cin >> x>>y;
        cin >> str1;
        cin >> str2;
        int flag=0;
        if (x>y)
        {
            cout << "NO\n";
            continue;
        }
        for(int i=0;i<x;i++)
        {
             arr1[(int)(str1[i])]+=1;
        }
          for(int i=0;i<y;i++)
        {
             arr2[(int)(str2[i])]+=1;
        }
        
        
        for (int k=0;k<200;k++)
        {
            if(arr1[k]>arr2[k])
            {
                flag=1;
            }
            if (flag==1){
                cout<<"NO\n";
                break;
            }
        }
        if (flag==0)
        {
            cout << "YES\n";
        }
        


    }

    
}