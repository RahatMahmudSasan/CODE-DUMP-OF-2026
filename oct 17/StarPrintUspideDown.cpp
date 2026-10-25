#include <iostream>
using namespace std;
    int main(){

        int row = 5;
        for(int i=row;i>=1;i--){
            for(int col=1; col<=i; col++){
                cout<<"* ";
            }
            cout<<endl;
        }




    return 0;

    }
