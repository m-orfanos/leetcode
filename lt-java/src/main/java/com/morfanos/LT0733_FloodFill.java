package com.morfanos;

import java.util.Stack;

class LT0733_FloodFill {

    static int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color) {
            return image;
        }

        record Point(int x, int y) {
        }
        var NORTH = new Point(-1, 0);
        var EAST = new Point(0, 1);
        var SOUTH = new Point(1, 0);
        var WEST = new Point(0, -1);
        var DIRECTIONS = new Point[] { NORTH, EAST, SOUTH, WEST };

        var oc = image[sr][sc];

        Stack<Point> q = new Stack<>();
        q.add(new Point(sr, sc));
        while (!q.isEmpty()) {
            var p = q.pop();
            if (image[p.x][p.y] == oc) {
                image[p.x][p.y] = color;
                for (Point d : DIRECTIONS) {
                    var x = p.x + d.x;
                    var y = p.y + d.y;
                    if (0 <= x && x < image.length && 0 <= y && y < image[x].length) {
                        q.add(new Point(x, y));
                    }
                }
            }
        }

        return image;
    }

}
