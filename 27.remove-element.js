/*
 * @lc app=leetcode id=27 lang=javascript
 *
 * [27] Remove Element
 */
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
let removeElement = function (nums, val) {
    if (nums.length === 0) return nums.length;
    if (nums.indexOf(val) < 0) return nums.length;
    let count = 0;
    for (let i = 0, max = nums.length; i < max; i++) {
        if (nums[i] != val) {
            nums[count++] = nums[i];
        }
    }
    return count;
};

