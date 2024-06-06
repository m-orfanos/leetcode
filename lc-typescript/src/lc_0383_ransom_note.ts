import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function can_construct(ransomNote: string, magazine: string): boolean {
    if (ransomNote.length > magazine.length) {
        return false;
    }

    const counter = "abcdefghijklmnopqrstuvwxyz".split("").reduce((acc, curr) => ({
        ...acc,
        [curr]: 0,
    }), {} as { [key: string]: number });

    for (const ch of magazine) {
        counter[ch] += 1;
    }

    for (const ch of ransomNote) {
        counter[ch] -= 1;
        if (counter[ch] < 0) {
            return false;
        }
    }

    return true;
};

Deno.test("0383 Random Note", () => {
    const test_cases: [string, string, boolean][] = [
        ["a", "b", false],
        ["aa", "ab", false],
        ["aa", "aab", true]
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const ransomNote = test_case[0];
        const magazine = test_case[1];

        const expected = test_case[2];
        const actual = can_construct(ransomNote, magazine);

        assertEquals(actual, expected);
    }
});
