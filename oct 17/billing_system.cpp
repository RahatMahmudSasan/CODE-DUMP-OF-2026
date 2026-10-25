#include <iostream>
using namespace std;
    int main(){
        int q;
        int total=0;
        int temp=0;
        bool AddItem;

        do{
            char option;
            cout<<"enter option b=burger,p=pizza and j=juice: "<<endl;
            cin>>option;
            if (option=='b'){
                cout<<"Enter berger quantity: "<<endl;
                cin>>q;
                total = 250 * q;
                temp=total + temp;
            }
            else if(option='p'){
                cout<<"Enter pizza quantity: "<<endl;
                cin>>q;
                total = 560 * q;
                temp=total + temp;
            }
            else if(option=='j'){
                cout<<"Enter juice quantity: "<<endl;
                cin>>q;
                total = 160 * q;
                temp=total + temp;
            }
            else{
                cout<<"invalid";
            }

            cout<<"Add more?Press 1 to, O the exit"<<endl;
            cin>>AddItem;
        }while(AddItem);
        cout<<"The total is: "<<temp<<endl;

    return 0;
    }

