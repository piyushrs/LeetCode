#include <vector>
#include <unordered_map>
#include <iostream>
#include <stdio.h>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // Brute-force solution with O(n^2) time complexity

        // int n = nums.size();
        // for(int i=0; i<(n-1); i++){
        //   for(int j=i+1; j<n; j++){
        //     if((nums[i]+nums[j]) == target){
        //       vector<int> ans {i,j};
        //       return ans;
        //     }
        //   }
        // }
        // return {};

      // Optimized solution with unordered map
      std::unordered_map<int, int> numMap;
      int n = nums.size();
      for (int i = 0; i < n; i++){
        int complement = target - nums[i];

        if (numMap.find(complement) != numMap.end()){
          return {i, numMap[complement]};
        }

        numMap[nums[i]] = i;
      }
      return {};
    }
};

int main(){
    Solution s;
    std::vector<int> nums {2, 7, 11, 15};
    int target = 9;
    std::cout<<"Result ";
    std::vector<int> ans = s.twoSum(nums, target);
    for(int i : ans){
      std::cout<< i<<" ";
    }
    return 0;
}