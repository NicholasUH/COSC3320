#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

int helper(vector<int> arr1, vector<int> arr2){
    int index, score, finalScore = 0;

    while(index < arr2.size()){
        while(score < arr1.size() and arr2[index] > arr1[score]){
            score++;
        }
        finalScore += score;
        index++;
    }
    return finalScore;
}

void merge(vector<int>& arr1, vector<int> &arr2 ,int left, int mid, int right, int& points1, int& points2) {
    
    // FIND MIDPOINTS
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    // MAKE SUBARRAYS
    vector<int> leftArr1(n1);
    vector<int> rightArr1(n2);
    vector<int> leftArr2(n1);
    vector<int> rightArr2(n2);
    
    for (int i = 0; i < n1; ++i){
        leftArr1[i] = arr1[left + i];
        leftArr2[i] = arr2[left + i];
    }

    for (int j = 0; j < n2; ++j){
        rightArr1[j] = arr1[mid + 1 + j];
        rightArr2[j] = arr2[mid + 1 + j];
    }
    
    
    int i1 = 0, i2 = 0, j1 = 0, j2 = 0;
    int k1 = left, k2 = left;
    
    
    if(i1 < leftArr1.size() && j1 < rightArr1.size()){
        points1 += helper(leftArr2,rightArr1);
        i1++;
    }
    
    if(i2 < leftArr2.size() && j2 < rightArr2.size()){
        points2 += helper(leftArr1,rightArr2);
        i2++;
    }
    
    
    // MERGE SUBARRAYS BACK

    i1 = 0, i2 = 0, j1 = 0, j2 = 0;
    k1 = left, k2 = left;

    while (i1 < n1 && j1 < n2) {
        if (leftArr1[i1] <= rightArr1[j1]) {
            arr1[k1] = leftArr1[i1];
            ++i1;
        }
        else {
            arr1[k1] = rightArr1[j1];
            ++j1;
        }
        ++k1;
    }
    
    while (i1 < n1) {
        arr1[k1] = leftArr1[i1];
        ++i1;
        ++k1;
    }

    while (j1 < n2) {
        arr1[k1] = rightArr1[j1];
        ++j1;
        ++k1;
    }
    
    while (i2 < n1 && j2 < n2) {
        if (leftArr2[i2] <= rightArr2[j2]) {
            arr2[k2] = leftArr2[i2];
            ++i2;
        }
        else {
            arr2[k2] = rightArr2[j2];
            ++j2;
        }
        ++k2;
    }

    while (i2 < n1) {
        arr2[k2] = leftArr2[i2];
        ++i2;
        ++k2;
    }

    while (j2 < n2) {
        arr2[k2] = rightArr2[j2];
        ++j2;
        ++k2;
    }
    
    
}

void mergeSort(vector<int> &arr1, vector<int> &arr2 , int left, int right, int& points1, int& points2) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        mergeSort(arr1, arr2, left, mid, points1, points2);
        mergeSort(arr1, arr2, mid + 1, right, points1, points2);

        merge(arr1, arr2, left, mid, right, points1, points2);
    }
}


int main(){

    vector<int> arr1;
    vector<int> arr2;
    string tempS;
    int tempI, points1 = 0, points2 = 0;

    // INPUT PARSING
    getline(cin, tempS);
    stringstream ss(tempS);
    while(ss >> tempI){
        arr1.push_back(tempI);
    }
    
    getline(cin, tempS);
    stringstream ss2(tempS);
    while(ss2 >> tempI){
        arr2.push_back(tempI);
    }
    
    mergeSort(arr1, arr2 ,0, arr1.size() - 1, points1, points2);

    for(int val : arr1){
        cout << val << " ";
    }

    cout << endl;
    
    for(int val : arr2){
        cout << val << " ";
    }
    
    cout << endl;
    
    cout << points1 << " " << points2;
    



}
// arr1 = robert
// arr2 = rachel




// 5 3 6 9
// 7 5 8 4
