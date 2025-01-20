import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function can_construct1(ransomNote: string, magazine: string): boolean {
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

function can_construct2(ransomNote: string, magazine: string): boolean {
    // const alphabet = "abcdefghijklmnopqrstuvwxyz";
    // alphabet.split("").forEach((l) => console.log(l.charCodeAt(0)));
    // 97, 98, 99, ...,
  
    if (magazine.length < ransomNote.length) {
      return false;
    }
  
    const histogram: number[] = [];
    for (let i = 0; i < 26; i++) {
      histogram.push(0);
    }
  
    for (let i = 0; i < magazine.length; i++) {
      histogram[magazine.charCodeAt(i) - 97] += 1;
    }
  
    for (let j = 0; j < ransomNote.length; j++) {
      histogram[ransomNote.charCodeAt(j) - 97] -= 1;
    }
  
    return histogram.every((l) => l >= 0);
  }

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

        const actual1 = can_construct1(ransomNote, magazine);
        assertEquals(actual1, expected);

        const actual2 = can_construct2(ransomNote, magazine);
        assertEquals(actual2, expected);
    }
});
