/**
 * @param {number} K
 * @return {number}
 */
let smallestRepunitDivByK = function (K) {
    if (K % 2 === 0 || K % 5 === 0) -1;
    let n = 0;
    for (let i = 1; i <= K; ++i) {
        n = (n * 10 + 1) % K;
        if (n == 0) return i;
    }
    return -1;
};