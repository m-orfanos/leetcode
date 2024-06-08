import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";
import { TreeNode, array_to_tree } from "./shared/utils.ts";

function maximum_depth(root: TreeNode | null): number {
    function dfs(node: TreeNode | null): number {
        if (node == null) {
            return 0;
        }
        const left = 1 + dfs(node.left);
        const right = 1 + dfs(node.right);
        return Math.max(left, right);
    }
    return dfs(root);
}

Deno.test("0104 Maximum Depth of Binary Tree", () => {
    const test_cases: [(number | null)[], number][] = [
        [[3, 9, 20, null, null, 15, 7], 3],
        [[1, null, 2], 2],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const root = array_to_tree(test_case[0]);
        const expected = test_case[1];

        const actual = maximum_depth(root);
        assertEquals(actual, expected);
    }
});
