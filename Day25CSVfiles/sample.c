#include <stdio.h>
#define n 5

int main()
{
    int ch = 1,i,j = 1,rear = 0,front = 0,queue[n],x = n;

    while(ch)
    {
        printf("Enter the choice :");
        scanf("%d",&ch);

        switch(ch)
        {
            case 1:
                if(rear == x)
                {
                    printf("The queue is full");
                }
                else{
                    printf("Enter the num :");
                    scanf("%d",queue[rear++]);
                }
                break;
            case 2:
                if(front == rear){
                    printf("The queue is empty");
                }
                printf("the deketed num is %d",queue[front++]);
                x++;
                break;

            case 3:

                
        }
    }
}
