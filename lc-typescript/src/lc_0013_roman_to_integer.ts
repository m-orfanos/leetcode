import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function roman_to_integer1(s: string): number {
    const symbols: { [key: string]: number } = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    };

    const adjust: { [key: string]: number } = {
        "IV": 2,
        "IX": 2,
        "XL": 20,
        "XC": 20,
        "CD": 200,
        "CM": 200,
    };

    let ans = 0;
    for (let i = 0; i < s.length; i += 1) {
        const si = s[i];
        const sj = s[i + 1];
        ans += symbols[si] - (adjust[si + sj] || 0);
    }

    return ans;
}

function roman_to_integer2(s: string): number {
    const mx: { [key: string]: number } = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    };

    let ans = 0;
    for (let i = 0; i < s.length - 1; i++) {
        const coef = mx[s[i]] < mx[s[i + 1]] ? -1 : 1;
        ans += coef * mx[s[i]];
    }

    ans += mx[s[s.length - 1]];

    return ans;
}

Deno.test("0013 Roman to Integer", () => {
    const test_cases: [string, number][] = [
        ["III", 3],
        ["LVIII", 58],
        ["MCMXCIV", 1994],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const s = test_case[0];
        const expected = test_case[1];

        const actual1 = roman_to_integer1(s);
        assertEquals(actual1, expected);

        const actual2 = roman_to_integer2(s);
        assertEquals(actual2, expected);
    }
});
