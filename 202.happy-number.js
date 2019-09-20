/*
 * @lc app=leetcode id=202 lang=javascript
 *
 * [202] Happy Number
 */
/**
 * @param {number} n
 * @return {boolean}
 */
let isHappy = function (n) {
    let set = new Set();
    function cal(n) {
        let sum = 0;
        while (n > 0) {
            sum += (n % 10) * (n % 10);
            n = Math.floor(n / 10);
        }
        return sum;
    }
    while (!set.has(n)) {
        set.add(n);
        n = cal(n);
        if (n === 1)
            return true;
    }
    return false;
};

