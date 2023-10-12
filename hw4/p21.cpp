// 2edc45a2-35ae-4259-9f85-64eca275858a
#include <iostream>
#include <map>
#include <vector>

using namespace std;

bool isValid(string operand1, string operand2, string sum, map<char, char> &assignments)
{
    for (int x = 0; x < operand1.length(); x++)
    {
        operand1[x] = (assignments[operand1[x]]);
    }

    for (int x = 0; x < operand2.length(); x++)
    {
        operand2[x] = (assignments[operand2[x]]);
    }

    for (int x = 0; x < sum.length(); x++)
    {
        sum[x] = (assignments[sum[x]]);
    }

    return (stol(operand1) + stol(operand2)) == stol(sum);
}

bool solveForDigits(string symbols, string operand1, string operand2, string sum, map<char, char> &assignments, vector<bool> &usedNums, int idx)
{
    if (idx == symbols.size())
    {
        return isValid(operand1, operand2, sum, assignments);
    }

    for (char digit : "0123456789")
    {
        if (isdigit(digit) && !usedNums[digit - '0'])
        {
            assignments[symbols[idx]] = digit;
            usedNums[digit - '0'] = true;

            if (solveForDigits(symbols, operand1, operand2, sum, assignments, usedNums, idx + 1))
                return true;
            usedNums[digit - '0'] = false;
        }
    }

    return false;
}

int main(int argc, char *argv[])
{
    string symbols, i_operand1, i_operand2, sum;
    cin >> symbols >> i_operand1 >> i_operand2 >> sum;

    vector<bool> usedNums(10, false);
    map<char, char> assignments;

    if (solveForDigits(symbols, i_operand1, i_operand2, sum, assignments, usedNums, 0))
    {
        for (char c : symbols)
        {
            cout << assignments[c];
        }
    }
}