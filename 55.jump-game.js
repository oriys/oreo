/**
 * @param {number[]} nums
 * @return {boolean}
 */
let canJump = function (nums) {
    const len = nums.length;
    let cur = nums[0];
    for (let i = 0; i < len; i++) {
        if (i > cur) break;
        cur = Math.max(cur, i + nums[i]);
    }
    return cur >= len - 1;
};