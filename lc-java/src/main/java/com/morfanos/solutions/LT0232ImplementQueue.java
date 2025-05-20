package com.morfanos.solutions;

import java.util.Stack;

class LT0232ImplementQueue {

    public static class MyQueue {

        private Stack<Integer> s1;
        private Stack<Integer> s2;

        public MyQueue() {
            this.s1 = new Stack<>();
            this.s2 = new Stack<>();
        }

        public void push(int x) {
            moveFirst();
            s1.push(x);
        }

        public int pop() {
            moveSecond();
            return s2.pop();

        }

        public int peek() {
            moveSecond();
            return s2.peek();
        }

        public boolean empty() {
            return s1.isEmpty() && s2.isEmpty();
        }

        private void moveFirst() {
            while (!s2.isEmpty()) {
                s1.push(s2.pop());
            }
        }

        private void moveSecond() {
            while (!s1.isEmpty()) {
                s2.push(s1.pop());
            }
        }

    }

}
