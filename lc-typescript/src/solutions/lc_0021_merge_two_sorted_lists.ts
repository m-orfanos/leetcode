import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

import {
    array_to_linked_list,
    linked_list_to_array,
    ListNode,
} from "../shared/utils.ts";

function merge_two_lists1(
    list1: ListNode | null,
    list2: ListNode | null,
): ListNode | null {
    if (list1 == null || list2 == null) {
        return list1 || list2;
    }

    const arr1 = linked_list_to_array(list1);
    const arr2 = linked_list_to_array(list2);

    const arr3 = arr1.concat(arr2);

    arr3.sort();

    return array_to_linked_list(arr3);
}

function merge_two_lists2(
    list1: ListNode | null,
    list2: ListNode | null,
): ListNode | null {
    if (list1 == null || list2 == null) {
        return list1 || list2;
    }

    // create an empty node, simplifies code below
    // must be dropped before exit
    const ans = new ListNode();
    let ptr = ans;

    let ptr1: ListNode | null = list1;
    let ptr2: ListNode | null = list2;

    while (ptr1 != null && ptr2 != null) {
        let val;
        if (ptr1.val < ptr2.val) {
            val = ptr1.val;
            ptr1 = ptr1.next;
        } else {
            val = ptr2.val;
            ptr2 = ptr2.next;
        }

        ptr.next = new ListNode(val);
        ptr = ptr.next;
    }

    let rem = ptr1 || ptr2;
    while (rem != null) {
        ptr.next = new ListNode(rem.val);
        rem = rem.next;
        ptr = ptr.next;
    }

    return ans.next;
}

Deno.test("0021 Merge Two Sorted Lists", () => {
    const test_cases = [
        [[1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]],
        [[], [], []],
        [[], [0], [0]],
        [[5], [1, 2, 4], [1, 2, 4, 5]],
        [[1, 2, 4], [5], [1, 2, 4, 5]],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const arr1 = test_case[0];
        const arr2 = test_case[1];

        const list1 = array_to_linked_list(arr1);
        const list2 = array_to_linked_list(arr2);

        const expected = test_case[2];

        const list3 = merge_two_lists1(list1, list2);
        const actual = linked_list_to_array(list3);

        assertEquals(actual, expected);
    }

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const arr1 = test_case[0];
        const arr2 = test_case[1];

        const list1 = array_to_linked_list(arr1);
        const list2 = array_to_linked_list(arr2);

        const expected = test_case[2];

        const list3 = merge_two_lists2(list1, list2);
        const actual = linked_list_to_array(list3);

        assertEquals(actual, expected);
    }
});
