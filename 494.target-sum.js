/*
 * @lc app=leetcode id=494 lang=javascript
 *
 * [494] Target Sum
 */
/**
 * @param {number[]} nums
 * @param {number} S
 * @return {number}
 */
var findTargetSumWays = function (nums, S) {
    let count = 0;
    function calculate(nums, i, sum, S) {
        if (i == nums.length) {
            if (sum == S)
                count++;
        } else {
            calculate(nums, i + 1, sum + nums[i], S);
            calculate(nums, i + 1, sum - nums[i], S);
        }
    }
    calculate(nums, 0, 0, S);
    return count;
};

