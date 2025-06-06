package com.morfanos.solutions;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Stack;

class LT0207CourseSchedule {

    static boolean canFinish(int numCourses, int[][] prerequisites) {
        var adjList = new HashMap<Integer, List<Integer>>();
        for (var i = 0; i < numCourses; i++) {
            adjList.put(i, new ArrayList<>());
        }

        for (var p : prerequisites) {
            adjList.get(p[0]).add(p[1]);
        }

        final var TODO = 0;
        final var DOING = 1;
        final var DONE = 2;
        var state = new int[numCourses];

        for (var i = 0; i < numCourses; i++) {
            if (state[i] == DONE) {
                continue;
            }

            // traverse
            var stk = new Stack<Integer>();
            stk.push(i);
            while (!stk.isEmpty()) {
                var n = stk.peek(); // peek, NOT pop
                var l = stk.size();
                state[n] = DOING;

                for (var adj : adjList.get(n)) {
                    if (state[adj] == DOING) {
                        return false;
                    }
                    if (state[adj] == TODO) {
                        stk.push(adj);
                    }
                }

                if (stk.size() - l == 0) {
                    // pop only when all prereqs are done
                    stk.pop();
                    state[n] = DONE;
                }
            }
        }

        return true;
    }

}
