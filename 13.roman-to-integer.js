/*
 * @lc app=leetcode id=13 lang=javascript
 *
 * [13] Roman to Integer
 */
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
    const map = new Map([['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000]]);
    if (s.length === 1)
        return map.get(s[0]);
    let ans = 0;
    for (let i = 0; i < s.length; i++) {
        const v1 = map.get(s[i]);
        const v2 = map.get(s[i + 1]);
        if (v2 > v1) {
            ans += v2 - v1;
            i++;
        } else {
            ans += v1;
        }
    }
    return ans;
};

