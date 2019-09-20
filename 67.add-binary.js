/*
 * @lc app=leetcode id=67 lang=javascript
 *
 * [67] Add Binary
 */
/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
let addBinary = function (a, b) {
    if (a.length < b.length) {
        let tmp = a;
        a = b;
        b = tmp;
    }
    let res = "";
    let carry = 0;
    for (let i = 1; i <= a.length; i++) {
        let m = parseInt(a[a.length - i]);
        let n = parseInt(b[b.length - i]) || 0;
        let add = m + n + carry;
        if (add === 3) {
            res = "1" + res;
            carry = 1;
        } else if (add === 2) {
            res = "0" + res;
            carry = 1;
        } else {
            res = add + res;
            carry = 0;
        }
    }
    if (carry === 1) {
        res = "1" + res;
    }
    return res;
};

