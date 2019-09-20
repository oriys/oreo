/*
 * @lc app=leetcode id=118 lang=javascript
 *
 * [118] Pascal's Triangle
 */
/**
 * @param {number} numRows
 * @return {number[][]}
 */
let generate = function (numRows) {
    const result = [];
    for (let i = 0; i < numRows; i++) {
        let row = [];
        for (let j = 0; j <= i; j++) {
            if (j === 0) {
                row.push(1);
            }
            else if (j === i) {
                row.push(1);
            }
            else{
                row.push(result[i-1][j-1]+result[i-1][j])
            }
        }
        result.push(row);
    }
    return result;
};
