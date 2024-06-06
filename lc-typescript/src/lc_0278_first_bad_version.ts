import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function first_bad_version1(n: number, isBadVersion: (v: number) => boolean): number {
    let curr = 1;
    while (curr <= n) {
        if (isBadVersion(curr)) {
            return curr;
        }
        curr += 1;
    }
    return -1;
}

function first_bad_version2(n: number, isBadVersion: (v: number) => boolean): number {
    let low = 1;
    let high = n;
    while (low <= high) {
        const mid = Math.floor(low + (high - low) / 2);
        if (isBadVersion(mid)) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return low;
}

Deno.test("0278 First Bad Version", () => {
    const test_cases = [
        [5, 4, 4],
        [5, 2, 2],
        [1, 1, 1],
        [3, 2, 2],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const n = test_case[0];
        const bad = test_case[1];

        const expected = test_case[2];

        const actual1 = first_bad_version1(n, (v: number) => v >= bad);
        const actual2 = first_bad_version2(n, (v: number) => v >= bad);

        assertEquals(actual1, expected);
        assertEquals(actual2, expected);
    }
});
