// c125482c-2506-4ef8-8ee3-3877bbb7d4aa
#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int findMaximumDifference(int n, vector<int> nums){
    int left = 0, right = 1, curr_max = 0;

    while(right < n){
        if(nums[left] < nums[right]){
            curr_max = max(curr_max, nums[right] - nums[left]);
        }
        else{
            left = right;
        }
        right++;
    }

    return curr_max;
}

int main(){

    int n, intTemp;
    vector<int> nums;
    string temp;


    cin >> n;
    cin.ignore();
    getline(cin,temp);
    stringstream ss(temp);

    while(ss >> intTemp){
        nums.push_back(intTemp);
    }
    
    cout << findMaximumDifference(n, nums) << endl;

    return 0;
}