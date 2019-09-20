/**
 * @param {string} S
 * @param {number} N
 * @return {boolean}
 */
let queryString = function (S, N) {
    for (let i = 1; i <= N; i++) {
        let sub = i.toString(2);
        if (S.indexOf(sub) === -1) return false;
    }
    return true;
};