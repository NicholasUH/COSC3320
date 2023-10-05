// ff7c2788-81ab-4c54-8f02-19014ac3a129
#include <iostream>
#include <map>
#include <vector>

using namespace std;

bool isValid(string op1, string op2, string sum, map<char, char>& assignments) {
    int operand1 = 0, operand2 = 0, ans = 0;

    string temp = "";

    for(char c: op1){
        operand1 = operand1 * 10 + (assignments.at(c) - '0');
    }

    for(char c: op2){
        operand2 = operand2 * 10 + (assignments.at(c) - '0');
    }
        

    for(char c: sum){
        ans = ans * 10 + (assignments.at(c) - '0');
    }

    return (operand1 + operand2) == ans;
}

bool solveForDigits(string symbols, string op1, string op2, string sum, map<char, char>& assignments, vector<bool>& usedNums, int idx) {
    if(idx == symbols.size()){
        return isValid(op1, op2, sum, assignments);
    }

    for(char digit: "0123456789") {
        if(isdigit(digit) && !usedNums[digit - '0']) {
            assignments[symbols[idx]] = digit;
            usedNums[digit - '0'] = true;
            
            if(solveForDigits(symbols, op1, op2, sum, assignments, usedNums, idx+1))
                return true;
            usedNums[digit - '0'] = false;
        }
    }

    return false;
}

int main(int argc, char *argv[]) {
    string symbols, operand1, operand2, sum;
    cin >> symbols >> operand1 >> operand2 >> sum;

    vector<bool> usedNums(10, false);
    map<char, char> assignments;

    string output = "";
    if(solveForDigits(symbols, operand1, operand2, sum, assignments, usedNums, 0)) {
        for(char c: symbols)
            output += assignments[c];
    }

    cout << output << endl;
}
