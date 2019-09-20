/**
 * @param {number[][]} A
 * @return {number}
 */
let numEnclaves = function (A) {
    let inbox = function (x, y, row, col) {
        if (x >= 0 && x < row && y >= 0 && y < col) {
            return true;
        }
        return false;
    }
    const row = A.length;
    const col = A[0].length;
    let dfs = function (x, y) {
        if (inbox(x, y, row, col) && A[x][y] === 1) {
            A[x][y] = 0;
            dfs(x - 1, y);
            dfs(x + 1, y);
            dfs(x, y - 1);
            dfs(x, y + 1);
        }
    }
    for (let i = 0; i < row; i++) {
        dfs(i, 0);
        dfs(i, col - 1);
    }
    for (let i = 0; i < col; i++) {
        dfs(0, i);
        dfs(row - 1, i);
    }
    let sum = 0;
    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            sum += A[i][j];
        }
    }
    return sum;
};