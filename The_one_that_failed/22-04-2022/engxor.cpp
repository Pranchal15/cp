#include<iostream>
using namespace std;
#define ll long long int
#define endl "\n"
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        ll n,q;
        cin >> n>>q;
        int c[2]{0};
        for (int i =0;i<n;i++)
        {
            int num;
            cin >> num;
            c[__builtin_popcount(num)%2]++;

        }
        while (q--)
        {
            int p;
            cin >> p;
            int z = __builtin_popcount(p);
            if(z%2==0)
            cout << c[0] << " "<< c[1] << endl;
            else 
            cout << c[1] << " "<< c[0] << endl;
        }

    }
}