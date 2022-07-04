#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

   char str1[100],str2[100];
   int n,t,i,j;
    scanf("%d",&t);
    while(t)
    {
    scanf("%d",&n);
   scanf("%s", &str1);
   scanf("%s", &str2); 
   for(i=0;i<n;i++)
   {   
       printf("%c%c",str1[i],str2[i]);
   }
   printf("\n");
        t=t-1;
    }
 
   return 0;

}