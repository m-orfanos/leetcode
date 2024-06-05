import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";
import { TreeNode, array_to_tree } from "./shared/utils.ts";

function is_balanced(root: TreeNode | null): boolean {
    function dfs(node: TreeNode | null): number {
        if (node == null) {
            return 0;
        }

        const left = dfs(node.left);
        if (left < 0) {
            return -1;
        }

        const right = dfs(node.right);
        if (right < 0) {
            return -1;
        }

        const diff = left > right ? left - right : right - left;
        if (diff > 1) {
            return -1;
        }

        return 1 + Math.max(left, right);
    }

    return dfs(root) != -1;
};

Deno.test("0110 Balanced Binary Tree", () => {
    const test_cases: [(number | null)[], boolean][] = [
        [[3, 9, 20, null, null, 15, 7], true],
        [[1, 2, 2, 3, 3, null, null, 4, 4], false],
        [[], true],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const root = array_to_tree(test_case[0]);

        const expected = test_case[1];
        const actual = is_balanced(root);

        assertEquals(actual, expected);
    }
});
