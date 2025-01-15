package com.morfanos.solutions;

import static com.morfanos.shared.Helper.toGraph;
import static com.morfanos.solutions.LT0133CloneGraph.cloneGraph;
import static com.morfanos.shared.Helper.toAdjList;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;

import org.junit.jupiter.api.Test;

class LT0133CloneGraphTest {

    @Test
    void cloneGraph11() {
        // list -> graph
        var expected = List.of(
                List.of(2, 4),
                List.of(1, 3),
                List.of(2, 4),
                List.of(1, 3));
        var node = toGraph(expected);

        // clone -> list
        var clone = cloneGraph(node);
        var actual = toAdjList(clone);

        assertEquals(expected, actual);
    }

}
