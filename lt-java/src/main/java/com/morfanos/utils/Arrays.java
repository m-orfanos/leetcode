package com.morfanos.utils;

public class Arrays {

    public static int[] toArray(int... ns) {
        return ns;
    }

    @SuppressWarnings("unchecked")
    public static <T> T[] toArray(T... ts) {
        return ts;
    }

}
