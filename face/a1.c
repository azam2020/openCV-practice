#include<stdio.h>
#include<stdlib.h>

int main()
{
 printf("Do you want to recognise a face?\n");
 char choice;
 scanf("%c",&choice);
 if(choice=='y' || choice=='Y')
{
 system("python3 a.py");
}
else if(choice=='n' || choice=='N')
{
 printf("Thank you, see you again\n");
}
else
{ 
 printf("Invalid choice\n");
}
return 0;
}
