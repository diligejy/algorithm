nums = [2,7,11,15] 
target = 9

// O(n^2) 풀이
var twoSum = function(nums, target) {
    for (let i = 0; i <= nums.length-1; i++) {
        for (let j = i+1; j <= nums.length; j++){
            if (nums[i] + nums[j] === target) {
                return [i, j]
            }
        }
    }
};