package com.morfanos.solutions;

import java.util.LinkedList;

class LT0542ZeroOneMatrix {

    static int[][] updateMatrix(int[][] mat) {
        // the choice of stack vs. queue is important
        // prioritize updating immediate neighbors
        // (e.g. in this case BFS >>>> DFS)

        // find all zeroes
        var q = new LinkedList<int[]>();
        for (var i = 0; i < mat.length; i++) {
            for (var j = 0; j < mat[i].length; j++) {
                if (mat[i][j] == 0) {
                    q.add(new int[] { i, j });
                } else {
                    mat[i][j] = Integer.MAX_VALUE;
                }
            }
        }

        // "flood fill" starting from zeroes
        var dirs = new int[][] { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
        while (!q.isEmpty()) {
            var n = q.poll();
            var x = n[0];
            var y = n[1];

            for (var i = 0; i < dirs.length; i++) {
                var dir = dirs[i];
                var dx = dir[0];
                var dy = dir[1];
                if (0 <= x + dx
                        && x + dx < mat.length
                        && 0 <= y + dy
                        && y + dy < mat[x + dx].length
                        && mat[x][y] + 1 < mat[x + dx][y + dy]) {
                    mat[x + dx][y + dy] = mat[x][y] + 1;
                    q.add(new int[] { x + dx, y + dy });
                }
            }
        }

        return mat;
    }

}
