package com.morfanos;

class LT0208ImplementTrie {

    public static class Trie {

        private Trie[] children = new Trie[128];
        private boolean isWord = false;

        public Trie() {

        }

        public void insert(String word) {
            var n = this;
            for (var i = 0; i < word.length(); i++) {
                var ch = word.charAt(i);
                if (n.children[ch] == null) {
                    n.children[ch] = new Trie();
                }
                n = n.children[ch];
            }
            n.isWord = true;
        }

        public boolean search(String word) {
            var n = this;
            for (var i = 0; i < word.length(); i++) {
                var ch = word.charAt(i);
                if (n.children[ch] == null) {
                    return false;
                }
                n = n.children[ch];
            }
            return n.isWord;
        }

        public boolean startsWith(String prefix) {
            var n = this;
            for (var i = 0; i < prefix.length(); i++) {
                var ch = prefix.charAt(i);
                if (n.children[ch] == null) {
                    return false;
                }
                n = n.children[ch];
            }
            return true;
        }

    }

}
