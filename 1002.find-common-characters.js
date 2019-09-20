/*
 * @lc app=leetcode id=1002 lang=javascript
 *
 * [1002] Find Common Characters
 */
/**
 * @param {string[]} A
 * @return {string[]}
 */
var commonChars = function (A) {
    let map = new Map();
    for (let i = 0; i < A.length; i++) {
        for (let j = 0; j < A[i].length; j++) {
            if (map.get(A[i][j]) === undefined) {
                let tmp = [];
                tmp[i] = 1;
                map.set(A[i][j], tmp);
            } else {
                let tmp = map.get(A[i][j]);
                tmp[i] = (tmp[i] || 0) + 1;
                map.set(A[i][j], tmp);
            }
        }
    }
    let result = [];
    map.forEach((v, k) => {
        if (!v.includes(undefined) && v.length===A.length) {
            result = result.concat(new Array(Math.min(...v)).fill(k));
        }
    });
    return result;
};