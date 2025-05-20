package com.morfanos.solutions;

import java.util.ArrayList;

class LT0973KClosestPoints {

    static int[][] kClosest(int[][] points, int k) {
        var l = new ArrayList<int[]>();
        for (var p : points) {
            var d = p[0] * p[0] + p[1] * p[1];
            l.add(new int[] { d, p[0], p[1] });
        }
        l.sort((a, b) -> a[0] - b[0]);

        var t = new int[k][2];
        for (var i = 0; i < t.length; i++) {
            t[i] = new int[] { l.get(i)[1], l.get(i)[2] };
        }

        return t;
    }

}
