#include<stdio.h>
void main()
  {
    int x,y;
    clrsccr();
    printf("Enter a number:");
    scanf("%d",&x);
    clrscr();
    do
      {
        printf("Guess the number");
        scanf("%d",&y);
        if(x>y)
          printf("Too Low !!!\n);
        else if(x<y)
          printf("Too High !!!\n);
        else
          printf("Spot on");
       }while(x!=y);
   }
        
        
