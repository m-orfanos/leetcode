import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function can_attend(meetings: number[][]): boolean {
    meetings.sort((a, b) => a[0] - b[0]);
    for (let i = 0; i < meetings.length - 1; i += 1) {
        const [, ei] = meetings[i];
        const [sj,] = meetings[i + 1];
        if (ei > sj) {
            return false;
        }
    }
    return true;
}

Deno.test("0252 Meeting Rooms", () => {
    const test_cases: [number[][], boolean][] = [
        [[[0, 30], [5, 10], [15, 20]], false],
        [[[7, 10], [2, 4]], true],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const meetings = test_case[0];
        const expected = test_case[1];

        const actual = can_attend(meetings);
        assertEquals(actual, expected);
    }
});
