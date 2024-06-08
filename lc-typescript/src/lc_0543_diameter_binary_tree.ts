import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";
import { TreeNode, array_to_tree } from "./shared/utils.ts";

function diameter_binary_tree(root: TreeNode | null): number {
    function dfs(node: TreeNode | null): number[] {
        if (node == null) {
            return [0, 0];
        }

        const [lheight, ldiameter] = dfs(node.left);
        const [rheight, rdiameter] = dfs(node.right);

        const height = 1 + Math.max(lheight, rheight);
        const diameter = Math.max(lheight + rheight, ldiameter, rdiameter);

        return [height, diameter];
    }

    const [_, diameter] = dfs(root);

    return diameter;
}

Deno.test("0543 Diameter of Binary Tree", () => {
    const test_cases: [(number | null)[], number][] = [
        [[1, 2, 3, 4, 5], 3],
        [[1, 2], 1],
        [[
            4, -7, -3, null, null, -9, -3, 9, -7, -4, null,
            6, null, -6, -6, null, null, 0, 6, 5, null,
            9, null, null, -1, -4, null, null, null, -2], 8],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const nums = array_to_tree(test_case[0]);
        const expected = test_case[1];

        const actual = diameter_binary_tree(nums);
        assertEquals(actual, expected);
    }
});
