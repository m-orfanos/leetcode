import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";
import { ListNode, array_to_linked_list, linked_list_to_array } from "./shared/utils.ts";

function reverse_linked_list1(head: ListNode | null): ListNode | null {
    let l1: ListNode | null = head;
    let l2: ListNode | null = null;

    while (l1 != null) {
        const l1_tail = l1.next;
        l1.next = l2;
        l2 = l1;
        l1 = l1_tail;
    }

    return l2;
}

function reverse_linked_list2(head: ListNode | null): ListNode | null {
    function reverse(l1: ListNode | null, l2: ListNode | null) {
        if (l1 == null) {
            return l2;
        }
        const l1_tail = l1.next;
        l1.next = l2;
        l2 = l1;
        return reverse(l1_tail, l2);
    }
    return reverse(head, null);
}

Deno.test("0206 Reverse Linked List", async (t) => {
    function get_test_cases() {
        const test_cases: [number[], number[]][] = [
            [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],
            [[1, 2], [2, 1]],
            [[], []],
        ];
        return test_cases;
    }

    await t.step(`Iterative reverse linked list`, () => {
        const test_cases = get_test_cases();
        for (let i = 0; i < test_cases.length; i += 1) {
            const test_case = test_cases[i];

            const nums = array_to_linked_list(test_case[0]);

            const expected = test_case[1];
            const actual = linked_list_to_array(reverse_linked_list1(nums));

            assertEquals(actual, expected);
        }
    });

    await t.step(`Recursive reverse linked list`, () => {
        const test_cases = get_test_cases();
        for (let i = 0; i < test_cases.length; i += 1) {
            const test_case = test_cases[i];

            const nums = array_to_linked_list(test_case[0]);

            const expected = test_case[1];
            const actual = linked_list_to_array(reverse_linked_list2(nums));

            assertEquals(actual, expected);
        }
    });

});
