package com.morfanos.solutions;

import java.util.ArrayList;

class LT0994RottingOranges {

    static int orangesRotting(int[][] grid) {
        // var EMPTY = 0;
        var FRESH = 1;
        var ROTTEN = 2;

        var ds = new int[][] { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

        var t = 0;
        while (true) {
            var rs = new ArrayList<int[]>();
            for (var i = 0; i < grid.length; i++) {
                for (var j = 0; j < grid[i].length; j++) {
                    var current = grid[i][j];
                    if (current != ROTTEN) {
                        continue;
                    }

                    for (int[] d : ds) {
                        var x = i + d[0];
                        var y = j + d[1];
                        if (0 <= x && x < grid.length
                                && 0 <= y && y < grid[x].length
                                && grid[x][y] == FRESH) {
                            rs.add(new int[] { x, y });
                        }
                    }
                }
            }

            if (rs.isEmpty()) {
                break;
            }

            for (int[] p : rs) {
                grid[p[0]][p[1]] = ROTTEN;
            }

            t += 1;
        }

        for (var i = 0; i < grid.length; i++) {
            for (var j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == FRESH) {
                    return -1;
                }
            }
        }

        return t;
    }

}
