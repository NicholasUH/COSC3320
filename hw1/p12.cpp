/*
Given an array of positive integers nums and a positive integer k, check whether it is 
possible to divide nums into sets of k consecutive numbers.

Write a recursive function to solve this problem. Return true if it is possible. 
Otherwise, return false. The input has 2 lines. The first line is the array of positive 
integers nums. The second line is the positive integer k.
*/

// e3fc3919-8de9-4d8d-a274-496b820bc2cf

#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

bool divideConsecutive(vector<int>& nums, int k) {
    if (nums.empty()) {
        return true;
    }

    if (nums.size() % k != 0) {
        return false;
    }

    int minNum = *min_element(nums.begin(), nums.end());

    for (int i = 0; i < k; ++i) {
        
        auto it = find(nums.begin(), nums.end(), minNum + i);

        if (it != nums.end()) {
            nums.erase(it); 
        } else {
            return false;
        }
    }

    return divideConsecutive(nums, k);
}

int main() {
    
    vector<int> nums;
    int k;
    string temp;
    int intTemp;

    getline(cin,temp);

    stringstream ss(temp);

    while(ss >> intTemp){
        nums.push_back(intTemp);
    }
    cin >> k;
    

    if (divideConsecutive(nums, k)) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }

    return 0;
}

