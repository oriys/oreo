/*
 * @lc app=leetcode id=268 lang=javascript
 *
 * [268] Missing Number
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
    const n = nums.length;
    return n * (n + 1) / 2 - nums.reduce((x, y) => x + y);
};

