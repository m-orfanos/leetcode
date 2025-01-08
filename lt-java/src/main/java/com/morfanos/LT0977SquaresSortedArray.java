package com.morfanos;

class LT0977SquaresSortedArray {

    static int[] sortedSquares(int[] ns) {
        var ans = new int[ns.length];
        var i = ns.length - 1;
        var lhs = 0;
        var rhs = ns.length - 1;
        while (lhs <= rhs) {
            var l = ns[lhs] * ns[lhs];
            var r = ns[rhs] * ns[rhs];
            if (l > r) {
                ans[i] = l;
                lhs += 1;
            } else {
                ans[i] = r;
                rhs -= 1;
            }
            i -= 1;
        }
        return ans;
    }

}
