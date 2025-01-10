package com.morfanos;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class LT0208ImplementTrieTest {

    @Test
    void trieTest1() {
        var t = new LT0208ImplementTrie.Trie();
        t.insert("apple");

        assertTrue(t.search("apple"));
        assertFalse(t.search("app"));
        assertTrue(t.startsWith("app"));

        t.insert("app");

        assertTrue(t.search("app"));
    }

}
