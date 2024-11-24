import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function add_binary1(a: string, b: string): string {
    const aa = parseInt(a, 2);
    const bb = parseInt(b, 2);
    const sum = aa + bb;
    return sum.toString(2);
}

function add_binary2(a: string, b: string): string {
    const size = a.length > b.length ? a.length : b.length;
    const ans = [];
    let carry = 0;
    for (let i = 0; i < size; i += 1) {
        const m = (a[a.length - 1 - i] || "0") === "0" ? 0 : 1;
        const n = (b[b.length - 1 - i] || "0") === "0" ? 0 : 1;
        const curr = carry + m + n;
        // curr
        // 0 0b00
        // 1 0b01
        // 2 0b10
        // 3 0b11
        if (curr === 0) {
            ans.push("0");
            carry = 0;
        } else if (curr === 1) {
            ans.push("1");
            carry = 0;
        } else if (curr === 2) {
            ans.push("0");
            carry = 1;
        } else if (curr === 3) {
            ans.push("1");
            carry = 1;
        }
    }

    if (carry > 0) {
        ans.push("1");
    }

    return ans.reverse().join("");
}

function add_binary3(a: string, b: string): string {
    const [sm, lg] = a.length < b.length ? [a, b] : [b, a];

    let ans = "";
    let carry = "0";
    for (let i = 0; i < lg.length; i++) {
        const x = i < sm.length ? sm[sm.length - 1 - i] : "0";
        const y = lg[lg.length - 1 - i];

        let tmp;
        if (x === "0" && y === "0" && carry === "0") {
            tmp = "0";
            carry = "0";
        } else if (x === "0" && y === "0" && carry === "1") {
            tmp = "1";
            carry = "0";
        } else if (x === "0" && y === "1" && carry === "0") {
            tmp = "1";
            carry = "0";
        } else if (x === "0" && y === "1" && carry === "1") {
            tmp = "0";
            carry = "1";
        } else if (x === "1" && y === "0" && carry === "0") {
            tmp = "1";
            carry = "0";
        } else if (x === "1" && y === "0" && carry === "1") {
            tmp = "0";
            carry = "1";
        } else if (x === "1" && y === "1" && carry === "0") {
            tmp = "0";
            carry = "1";
        } else if (x === "1" && y === "1" && carry === "1") {
            tmp = "1";
            carry = "1";
        }

        ans = tmp + ans;
    }

    return carry === "1" ? carry + ans : ans;
}

Deno.test("0067 Add Binary", () => {
    const test_cases: [string, string, string][] = [
        ["11", "1", "100"],
        ["1010", "1011", "10101"],
        ["0", "0", "0"],
        ["100", "110010", "110110"],
        ["110010", "10111", "1001001"],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const a = test_case[0];
        const b = test_case[1];
        const expected = test_case[2];

        const actual1 = add_binary1(a, b);
        const actual2 = add_binary2(a, b);
        const actual3 = add_binary3(a, b);

        assertEquals(actual1, expected, `failed soln#1 for ${a} + ${b} == ${expected}`);
        assertEquals(actual2, expected, `failed soln#2 for ${a} + ${b} == ${expected}`);
        assertEquals(actual3, expected, `failed soln#3 for ${a} + ${b} == ${expected}`);
    }
});
