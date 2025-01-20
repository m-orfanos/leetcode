import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function flood_fill1(
    image: number[][],
    sr: number,
    sc: number,
    color: number,
): number[][] {
    const starting_color = image[sr][sc];

    const stack: [number, number][] = [[sr, sc]];
    while (stack.length > 0) {
        const [row, col] = stack.pop()!;
        if (image[row][col] !== starting_color || image[row][col] === color) {
            continue;
        }

        image[row][col] = color;

        if (row - 1 >= 0) {
            stack.push([row - 1, col]);
        }
        if (row + 1 < image.length) {
            stack.push([row + 1, col]);
        }
        if (col - 1 >= 0) {
            stack.push([row, col - 1]);
        }
        if (col + 1 < image[sr].length) {
            stack.push([row, col + 1]);
        }
    }

    return image;
}

function flood_fill2(
    image: number[][],
    sr: number,
    sc: number,
    color: number,
): number[][] {
    const scolor = image[sr][sc];
    if (scolor === color) {
        return image;
    }

    const stack = [[sr, sc]];
    while (stack.length > 0) {
        const [r, c] = stack.pop()!;
        image[r][c] = color;
        if (r + 1 < image.length && image[r + 1][c] === scolor) {
            stack.push([r + 1, c]);
        }
        if (c + 1 < image[r].length && image[r][c + 1] === scolor) {
            stack.push([r, c + 1]);
        }
        if (r - 1 >= 0 && image[r - 1][c] === scolor) {
            stack.push([r - 1, c]);
        }
        if (c - 1 >= 0 && image[r][c - 1] === scolor) {
            stack.push([r, c - 1]);
        }
    }

    return image;
}

Deno.test("0733 Flood Fill", () => {
    function get_test_cases() {
        const test_cases: [number[][], number, number, number, number[][]][] = [
            [
                [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
                1,
                1,
                2,
                [[2, 2, 2], [2, 2, 0], [2, 0, 1]],
            ],
            [
                [[0, 0, 0], [0, 0, 0]],
                0,
                0,
                0,
                [[0, 0, 0], [0, 0, 0]],
            ],
        ];
        return test_cases;
    }

    const ts1 = get_test_cases();
    for (let i = 0; i < ts1.length; i += 1) {
        const test_case = ts1[i];

        const image = test_case[0];
        const sr = test_case[1];
        const sc = test_case[2];
        const color = test_case[3];

        const expected = test_case[4];
        const actual = flood_fill1(image, sr, sc, color);

        assertEquals(actual, expected);
    }

    const ts2 = get_test_cases();
    for (let i = 0; i < ts2.length; i += 1) {
        const test_case = ts2[i];

        const image = test_case[0];
        const sr = test_case[1];
        const sc = test_case[2];
        const color = test_case[3];

        const expected = test_case[4];
        const actual = flood_fill2(image, sr, sc, color);

        assertEquals(actual, expected);
    }
});
