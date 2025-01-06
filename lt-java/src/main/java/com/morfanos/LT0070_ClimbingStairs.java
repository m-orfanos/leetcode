package com.morfanos;

import java.math.BigInteger;

class LT0070_ClimbingStairs {

    static int climbStairs1(int n) {
        // Fibonacci sequence :/
        var a = 0;
        var b = 1;
        while (n > 0) {
            var t = a;
            a = b;
            b += t;
            n -= 1;
        }
        return b;
    }

    private int comb(int n, int k) {
        // https://en.wikipedia.org/wiki/Combination#Example_of_counting_combinations
        var i = 0;
        var t = BigInteger.ONE; // numerator
        var b = BigInteger.ONE; // denominator
        while (i < k) {
            t = t.multiply(BigInteger.valueOf(n - i));
            b = b.multiply(BigInteger.valueOf(i + 1));
            i += 1;
        }
        return t.divide(b).intValue();
    }

    public int climbStairs(int n) {
        // combinatorics approach
        //
        // 1:1 {1}
        // 2:2 {1+1, 2}
        // 3:3
        // .....1+1+1 ..............| 3c3 = 3!/3!/0! = 1
        // .....2+1, 1+2 ...........| 2c1 = 2!/1!/1! = 2
        // 4:5
        // .....1+1+1+1 ............| 4c4 = 4!/4!/0! = 1
        // .....1+1+2, 1+2+1, 2+1+1 | 3c2 = 3!/2!/1! = 3
        // .....2+2 ................| 2c0 = 2!/0!/2! = 1
        // 5:8
        // .....1+1+1+1+1 .........................| 5c5 = 5!/5!/0! = 1
        // .....1+1+1+2, 1+1+2+1, 1+2+1+1, 2+1+1+1 | 4c3 = 4!/3!/1! = 4
        // .....2+2+1, 2+1+2, 1+2+2 ...............| 3c1 = 3!/1!/2! = 3
        var sum = 0;
        var a = n;
        var b = n;
        while (b >= 0) {
            sum += comb(a, b);
            a -= 1;
            b -= 2;
        }
        return sum;
    }

}
