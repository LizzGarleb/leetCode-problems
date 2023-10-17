/**
 * Brute Force Solution
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 * 
 * Time Complexity: O(n^2) (nested for loop)
 * Space Complexity: O(1) 
 */
var twoSum = (nums, target) => {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j]
            }
        }
    }
};
