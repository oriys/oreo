/*
 * @lc app=leetcode id=1108 lang=javascript
 *
 * [1108] Defanging an IP Address
 */
/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function (address) {
    let result = '';
    for (let i = 0; i < address.length; i++) {
        if (address[i] != '.') {
            result = result + address[i];
        } else {
            result = result + '[.]';
        }
    }
    return result;
};