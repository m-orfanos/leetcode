package com.morfanos;

class LT0155MinStack {

    public static class MinStack {

        private int[] stk = new int[30000];
        private int[] min = new int[30000];

        private int top = -1;

        public MinStack() {
        }

        public void push(int val) {
            if (top < 0) {
                top = 0;
                stk[top] = val;
                min[top] = val;
            } else {
                top += 1;
                stk[top] = val;
                min[top] = Math.min(min[top - 1], val);
            }
        }

        public void pop() {
            top -= 1;
        }

        public int top() {
            return stk[top];
        }

        public int getMin() {
            return min[top];
        }

    }

}
