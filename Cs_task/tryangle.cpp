#include<iostream>
using namespace std;
int main()
{
    int t,h;
    cin >> t;
    while (t--)
    {
        cin >> h;
        for (int i=0;i<h;i++)
        {
            for (int j=0;j<h;j++)
            {
                if (j==0)
                {
                    cout << "*";

                }
                else if (i==j)
                {
                    cout << "*";

                }
                else if (i==h-1)
                {
                    cout << "*";
                }
                else {
                    cout << " ";
                }
            }
            cout<< "\n";
        }

    }
    return 0;
}