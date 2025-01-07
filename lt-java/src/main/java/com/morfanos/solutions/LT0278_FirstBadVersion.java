package com.morfanos.solutions;

import java.util.function.Function;

class LT0278_FirstBadVersion {

    static int firstBadVersion(int n, Function<Integer, Boolean> isBadVersion) {
        var lhs = 1;
        var rhs = n;
        while (lhs <= rhs) {
            var mid = lhs + (rhs - lhs) / 2;
            if (isBadVersion.apply(mid)) {
                rhs = mid - 1;
            } else {
                lhs = mid + 1;
            }
        }
        return lhs;
    }

}
