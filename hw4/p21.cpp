#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

bool isValid(unordered_map<char, char> &assignments, string operand1, string operand2, string sum){

    int i_operand1, i_operand2, i_sum;
    
    for(int x = 0; x < operand1.length();x++){
        operand1[x] = assignments[operand1[x]];
    }
    for(int x = 0; x < operand2.length();x++){
        operand2[x] = assignments[operand2[x]];
    }
    for(int x = 0; x < sum.length();x++){
        sum[x] = assignments[sum[x]];
    }

    i_operand1 = stoi(operand1);
    i_operand2 = stoi(operand2);
    sum = stoi(sum);

    return i_operand1 + i_operand2 == i_sum;
}

bool backtrack(unordered_map<char, char> &assignments,string list, string operand1, string operand2, string sum, vector<bool> &used, int index = 0){
    
    if(index == assignments.size() - 1){
        return isValid(assignments,operand1, operand2,sum);
    }

    char symbol = list[index];
    for(char digit : "0123456789"){
        if(!used[digit - '0']){
            used[digit - '0'] = true;
            assignments[symbol] = digit;

            if(backtrack(assignments,list,operand1,operand2,sum,used,index++)){
                return true;
            }
            else{
                used[digit - '0'] = false;
            }
        }
    }
    
    return false;
}


int main(){
    
    string list, operand1, operand2, sum;
    cin >> list >> operand1 >> operand2 >> sum;
    unordered_map<char, char> assignments;
    vector<bool> used(10, false);

    for(char c : list){
        assignments[c] = -1;
    }

    backtrack(assignments, list, operand1, operand2,sum,used);

    for(char c : list){
        cout << assignments[c];
    }

    return 0;
}


