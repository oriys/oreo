/*
 * @lc app=leetcode id=88 lang=javascript
 *
 * [88] Merge Sorted Array
 */
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
let merge = function (nums1, m, nums2, n) {
    while (m > 0 && n > 0) {
        if (nums1[m - 1] > nums2[n - 1]) {
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        } else {
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        }
    }
    if (n > 0) {
        for (let i = 0; i < n; i++) {
            nums1[i] = nums2[i];
        }
    }
};

