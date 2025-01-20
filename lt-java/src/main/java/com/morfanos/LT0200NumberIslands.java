package com.morfanos;

import java.util.LinkedList;

class LT0200NumberIslands {

    static int numIslands(char[][] grid) {
        var cnt = 0;
        var ds = new int[][] { { 0, 1 }, { 0, -1 }, { 1, 0 }, { -1, 0 } };

        for (var i = 0; i < grid.length; i++) {
            for (var j = 0; j < grid[i].length; j++) {
                if (grid[i][j] != '1') {
                    continue;
                }
                cnt += 1;

                var q = new LinkedList<int[]>();
                q.add(new int[] { i, j });
                while (!q.isEmpty()) {
                    var p = q.poll();

                    if (grid[p[0]][p[1]] != '1') {
                        continue;
                    }

                    grid[p[0]][p[1]] = 2;

                    for (int[] d : ds) {
                        var x = p[0] + d[0];
                        var y = p[1] + d[1];
                        if (0 <= x && x < grid.length
                                && 0 <= y && y < grid[x].length
                                && grid[x][y] == '1') {
                            q.add(new int[] { x, y });
                        }
                    }
                }
            }
        }

        return cnt;
    }

}
