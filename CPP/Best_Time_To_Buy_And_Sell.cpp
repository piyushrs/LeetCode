#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int largestDiff = 0;
        int minVal = 10001;
        int n = prices.size();
        if(n == 1){
          return largestDiff;
        }
        for (int i = 0; i<n; i++){
            if (prices[i] < minVal){
                minVal = prices[i];
            }
            else if ((prices[i]-minVal) > largestDiff){
                largestDiff = prices[i] - minVal;
            }
            else{
              continue;
            }
        }
        return largestDiff;
    }
};

int main(){
    Solution s;
    vector<int> prices {7,1,5,3,6,4};
    int ans = s.maxProfit(prices);
    cout<<ans;
}