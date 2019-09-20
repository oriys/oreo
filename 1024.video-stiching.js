/**
 * @param {number[][]} clips
 * @param {number} T
 * @return {number}
 */
let videoStitching = function (clips, T) {
    clips.sort((a, b) => a[1] - b[1]);
    let cur = 0;
    let count = 0;
    let max = 0;
    if (clips[clips.length - 1][1] < T) return -1;
    for (let i = 0; i < clips.length && cur < T; i++) {
        for (let j = i; j < clips.length; j++) {
            if (clips[j][0] <= cur && clips[j][1] >= max && clips[j][1] > cur) {
                max = clips[j][1];
                i = j;
            }
        }
        if (max === 0) return -1;
        cur = max;
        count += 1;
    }
    return count;
};