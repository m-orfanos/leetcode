package com.morfanos;

class LT0191_Number1Bits {

    static int hammingWeight(int n) {
        var cnt = 0;
        while (n > 0) {
            cnt += n % 2;
            n /= 2;
        }
        return cnt;
    }

}
