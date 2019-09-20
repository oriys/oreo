/**
 * @param {number} N
 * @return {string}
 */
let baseNeg2 = function (N) {
    if (N === 0) return '0';
    let arr = [];
    while (N) {
        arr.push((N & 1) + '');
        N = -(N >> 1);
    }
    return arr.reverse().join('');
};