import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function is_palindrome1(s: string): boolean {
    function sanitize(s: string): string {
        let sanitized = "";
        for (let i = 0; i < s.length; i += 1) {
            const nb = s.charCodeAt(i);
            if (nb < 48) {
                continue;
            }
            const ch = s.charAt(i);
            // numbers taken from https://www.asciitable.com/
            if (48 <= nb && nb <= 57) {
                // 0-9
                sanitized += ch;
            } else if (65 <= nb && nb <= 90) {
                // A-Z
                sanitized += String.fromCharCode(nb + (97 - 65));
            } else if (97 <= nb && nb <= 122) {
                // a-z
                sanitized += ch;
            }
        }
        return sanitized;
    }

    function is_palindrome0(s: string): boolean {
        let ans = true;
        let left = 0;
        let right = s.length - 1;
        while (left < right) {
            if (s[left] != s[right]) {
                ans = false;
            }
            left += 1;
            right -= 1;
        }

        return ans;
    }

    return is_palindrome0(sanitize(s));
}

function is_palindrome2(s: string): boolean {
    function get_char(s: string, i: number): string | null {
        const nb = s.charCodeAt(i);
        const ch = s.charAt(i);
        // numbers taken from https://www.asciitable.com/
        if (48 <= nb && nb <= 57) {
            // 0-9
            return ch;
        } else if (65 <= nb && nb <= 90) {
            // A-Z
            return String.fromCharCode(nb + (97 - 65));
        } else if (97 <= nb && nb <= 122) {
            // a-z
            return ch;
        } else {
            // invalid character
            return null;
        }
    }

    let left = 0;
    let right = s.length - 1;
    while (left < right) {
        const lch = get_char(s, left);
        if (lch == null) {
            left += 1;
            continue;
        }
        const rch = get_char(s, right);
        if (rch == null) {
            right -= 1;
            continue;
        }

        if (lch != rch) {
            return false;
        }

        left += 1;
        right -= 1;
    }

    return true;
}

Deno.test("0125 Valid Palindrome", () => {
    const test_cases: [string, boolean][] = [
        ["A man, a plan, a canal: Panama", true],
        ["race a car", false],
        [" ", true],
        ["1b1", true],
        ["0P", false],
        ["ab@a", true],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const s = test_case[0];

        const actual1 = is_palindrome1(s);
        const actual2 = is_palindrome2(s);

        const expected = test_case[1];

        assertEquals(actual1, expected);
        assertEquals(actual2, expected);
    }
});
