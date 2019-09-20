/*
 * @lc app=leetcode id=38 lang=javascript
 *
 * [38] Count and Say
 */
/**
 * @param {number} n
 * @return {string}
 */
let countAndSay = function(n) {
    if(n <= 1) return "1";
    let cs = '1';
    for(let i = 2 ; i <= n ; i++){
        let num = cs.charAt(0); 
        let temp = cs;
        let count = 1;
        cs = '';
        for(let j = 1 ; j < temp.length; j++){
            if(temp.charAt(j) == num){
                count++;
            } else {
                cs += count;     
                cs += num;
                num = temp.charAt(j);
                count = 1;
            }
        }
        cs += count;     
        cs += num;
    }
    return cs;
};

