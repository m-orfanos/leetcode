import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function backspace_string_compare1(s: string, t: string): boolean {
    function sanitize(str: string) {
        const ans = [];

        let deletes = 0;
        let i = 0;
        while (i < str.length) {
            const ch = str[str.length - 1 - i];
            if (ch === "#") {
                deletes += 1;
            } else if (deletes > 0) {
                deletes -= 1;
            } else {
                ans.push(ch);
            }
            i += 1;
        }

        return ans.reverse().join("");
    }

    return sanitize(s) === sanitize(t);
}

function backspace_string_compare2(s: string, t: string): boolean {
    function sanitize(str: string): string {
        const stk: string[] = [];
        for (const ch of str) {
            if (ch !== "#") {
                stk.push(ch);
            } else if (stk.length > 0) {
                stk.pop();
            }
        }
        return stk.join("");
    }
    return sanitize(s) === sanitize(t);
}

function backspace_string_compare3(s: string, t: string): boolean {
    let si = 0;
    let sdels = 0;

    let ti = 0;
    let tdels = 0;

    // iterate over both strings
    // compare when find valid character
    while (si < s.length && ti < t.length) {
        if (s[s.length - 1 - si] === "#") {
            sdels += 1;
            si += 1;
        } else if (sdels > 0) {
            sdels -= 1;
            si += 1;
        } else if (t[t.length - 1 - ti] === "#") {
            tdels += 1;
            ti += 1;
        } else if (tdels > 0) {
            tdels -= 1;
            ti += 1;
        } else if (s[s.length - 1 - si] !== t[t.length - 1 - ti]) {
            return false;
        } else {
            si += 1;
            ti += 1;
        }
    }

    // finish processing both strings
    function is_done(str: string, idx: number, dels: number): boolean {
        while (idx < str.length) {
            if (str[str.length - 1 - idx] === "#") {
                dels += 1;
                idx += 1;
            } else if (dels > 0) {
                dels -= 1;
                idx += 1;
            } else {
                return false;
            }
        }
        return true;
    }

    return is_done(s, si, sdels) && is_done(t, ti, tdels);
}


Deno.test("0844 Backspace String Compare", () => {
    const test_cases: [string, string, boolean][] = [
        ["ab#c", "ad#c", true],
        ["ab##", "c#d#", true],
        ["a#c", "b", false],
        ["gtc#uz#", "gtcm##uz#", true],
        ["a##c", "#a#c", true],
        ["y#fo##f", "y#f#o##f", true],
        ["bxj##tw", "bxo#j##tw", true],
        ["bxj##tw", "bxj###tw", false],
        ["nzp#o#g", "b#nzp#o#g", true],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const s = test_case[0];
        const t = test_case[1];
        const expected = test_case[2];

        const actual1 = backspace_string_compare1(s, t);
        const actual2 = backspace_string_compare2(s, t);
        const actual3 = backspace_string_compare3(s, t);

        assertEquals(actual1, expected, `Failed for "${s}" & "${t}"`);
        assertEquals(actual2, expected, `Failed for "${s}" & "${t}"`);
        assertEquals(actual3, expected, `Failed for "${s}" & "${t}"`);
    }
});
