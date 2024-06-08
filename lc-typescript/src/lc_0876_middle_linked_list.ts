import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";
import { ListNode, array_to_linked_list, linked_list_to_array } from "./shared/utils.ts";

function middle_linked_list(head: ListNode | null): ListNode | null {
    let slow = head;
    let fast = head?.next || null;
    while (fast != null) {
        slow = slow?.next || null;
        fast = fast.next?.next || null;
    }
    return slow;
}

Deno.test("0876 Middle of Linked List", () => {
    const test_cases: [number[], number[]][] = [
        [[1, 2, 3, 4, 5], [3, 4, 5]],
        [[1, 2, 3, 4, 5, 6], [4, 5, 6]],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const head = array_to_linked_list(test_case[0]);
        const expected = test_case[1];

        const actual = linked_list_to_array(middle_linked_list(head));

        assertEquals(actual, expected);
    }
});
