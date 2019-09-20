/*
 * @lc app=leetcode id=53 lang=javascript
 *
 * [53] Maximum Subarray
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
let maxSubArray = function (nums) {
    if (nums.length === 1) {
        return nums[0];
    }
    let max = nums[0];
    for (let i = 1; i < nums.length; i++) {
        nums[i] = Math.max(nums[i],  nums[i] + nums[i - 1]);
        max = Math.max(max, nums[i]);
    }
    return max;
};

