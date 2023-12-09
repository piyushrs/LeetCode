#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> counts;
        int n = nums.size();
        for (int i = 0; i < n; i++){
            if (counts.find(nums[i]) != counts.end()){
                return true;
            }
            counts[nums[i]] = 1;
        }
        return false;
    }
};

int main(){
    Solution s;
    vector<int> nums {1,2,3,1};
    cout << s.containsDuplicate(nums);
    return 0;
}