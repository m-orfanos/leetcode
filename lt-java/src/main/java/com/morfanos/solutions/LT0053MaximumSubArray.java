package com.morfanos.solutions;

class LT0053MaximumSubArray {

    static int maxSubArray1(int[] ns) {
        var best = ns[0];
        var curr = ns[0];
        for (var i = 1; i < ns.length; i++) {
            curr = Math.max(ns[i], curr + ns[i]);
            best = Math.max(best, curr);
        }
        return best;
    }

    // **** Solution 2 **** //
    // Divide and conquer approach
    // Time complexity.: O(n*log(n))
    // Space complexity: O(log(n))
    private static int go(int[] ns, int lo, int hi) {
        // base case
        if (lo == hi) {
            return ns[lo];
        }

        var mid = lo + (hi - lo) / 2;

        // find the largest sum of elements
        // from mid to some point on the left
        var lcurr = 0;
        var lbest = Integer.MIN_VALUE;
        for (var i = mid; i >= lo; i--) {
            lcurr += ns[i];
            lbest = Math.max(lbest, lcurr);
        }

        // find the largest sum of elements
        // from mid to some point on the right
        var rcurr = 0;
        var rbest = Integer.MIN_VALUE;
        for (var i = mid; i <= hi; i++) {
            rcurr += ns[i];
            rbest = Math.max(rbest, rcurr);
        }

        // recursive step
        var best = lbest + rbest - ns[mid]; // ns[mid] is double counted
        var left = go(ns, lo, mid);
        var right = go(ns, mid + 1, hi);

        return Math.max(best, Math.max(left, right));
    }

    static int maxSubArray2(int[] ns) {
        return go(ns, 0, ns.length - 1);
    }

}
