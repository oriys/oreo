/**
 * @param {string} sub
 * @param {string} ptn
 * @return {boolean}
 */
let match = (sub, ptn, re) => {
    if (sub.length === 0) {
        if (ptn.length === 0) {
            return true;
        }
        return false;
    }
    if (ptn.length === 0) {
        return sub.match(re);
    }
    if (sub[0] === ptn[0]) {
        return match(sub.slice(1), ptn.slice(1), re);
    }
    return match(sub.slice(1), ptn, re);
}
/**
 * @param {string[]} queries
 * @param {string} pattern
 * @return {boolean[]}
 */
let camelMatch = function (queries, pattern) {
    let arr = [];
    let re = /(?=[A-Z])/;
    let filter = c => c.charCodeAt(0) >= 65 && c.charCodeAt(0) <= 90
    let len = pattern.split('').filter(filter).length;
    for (let query of queries) {
        if (query.split('').filter(filter).length !== len) {
            arr.push(false);
        }
        else {
            arr.push(match(query, pattern, re));
        }
    }
    return arr;
};