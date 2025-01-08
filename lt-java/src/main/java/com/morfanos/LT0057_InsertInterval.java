package com.morfanos;

import java.util.ArrayList;

class LT0057_InsertInterval {

    static int[][] insert(int[][] intervals, int[] newInterval) {
        // insert and sort
        var xss = new ArrayList<int[]>();
        for (var i = 0; i < intervals.length; i++) {
            xss.add(intervals[i]);
        }
        xss.add(newInterval);
        xss.sort((a, b) -> a[0] - b[0]);

        // loop
        var ans = new ArrayList<int[]>();
        ans.add(xss.get(0));
        for (var j = 1; j < xss.size(); j++) {
            var xs = xss.get(j);
            var si = xs[0];
            var ei = xs[1];

            var prev = ans.get(ans.size() - 1);
            var sp = prev[0];
            var ep = prev[1];

            if ((sp <= si && si <= ep) || (sp <= ei && ei <= ep)) {
                // intervals intersect, merge them
                var st = Math.min(sp, si);
                var et = Math.max(ep, ei);
                ans.set(ans.size() - 1, new int[] { st, et });
            } else {
                ans.add(new int[] { si, ei });
            }
        }

        // convert ArrayList<int[]> to int[][]
        var t = new int[ans.size()][2];
        return ans.toArray(t);
    }

}
