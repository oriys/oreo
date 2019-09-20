/*
 * @lc app=leetcode id=1122 lang=javascript
 *
 * [1122] Relative Sort Array
 */
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
let relativeSortArray = function (arr1, arr2) {
    let map = new Map();
    arr2.forEach((n,i) => { map.set(n, i) });
    arr1.forEach((n,i) => {
        map.set(n,map.get(n)===undefined ? 1000+n:map.get(n));
    });
    arr1.sort((x,y)=>map.get(x)-map.get(y));
    return arr1;
};
