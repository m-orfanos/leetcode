import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function is_anagram1(s: string, t: string): boolean {
    if (s.length !== t.length) {
        return false;
    }

    const counter = new Map<string, number>();
    for (const ch of s) {
        const cnt = counter.get(ch) || 0;
        counter.set(ch, cnt + 1);
    }

    for (const ch of t) {
        const cnt = counter.get(ch) || 0;
        if (cnt <= 0) {
            return false;
        }
        counter.set(ch, cnt - 1);
    }

    let sum = 0;
    for (const [_, cnt] of counter) {
        sum += cnt;
    }

    return sum == 0;
}

function is_anagram2(s: string, t: string): boolean {
    if (s.length !== t.length) {
        return false;
    }

    const s1 = s.split("").sort().join("");
    const t1 = t.split("").sort().join("");

    return s1 === t1;
}

function is_anagram3(s: string, t: string): boolean {
    if (s.length !== t.length) {
        return false;
    }

    const letters = new Array<number>(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        // a = 97, z = 122
        letters[s.charCodeAt(i) - 97] += 1;
        letters[t.charCodeAt(i) - 97] -= 1;
    }

    return letters.every((l) => l === 0);
}

Deno.test("0242 Valid Anagram", () => {
    const test_cases: [string, string, boolean][] = [
        ["anagram", "nagaram", true],
        ["rat", "car", false],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const s = test_case[0];
        const t = test_case[1];

        const actual1 = is_anagram1(s, t);
        const actual2 = is_anagram2(s, t);
        const actual3 = is_anagram3(s, t);

        const expected = test_case[2];

        assertEquals(actual1, expected);
        assertEquals(actual2, expected);
        assertEquals(actual3, expected);
    }
});
