import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";
import { ListNode, array_to_linked_list } from "../shared/utils.ts";

function is_palindrome(head: ListNode | null): boolean {
  let rev: ListNode | null = null;
  let slow: ListNode | null = head;
  let fast: ListNode | null = head;
  while (slow != null && fast != null) {
    if (fast.next == null) {
      // list has odd-length, skips middle element
      slow = slow.next;
      break;
    }
    fast = fast.next.next;

    // build reverse
    const tmp: ListNode | null = slow.next;
    slow.next = rev;
    rev = slow;
    slow = tmp;
  }

  while (slow != null && rev != null) {
    if (slow.val !== rev.val) {
      return false;
    }
    rev = rev.next;
    slow = slow.next;
  }

  return true;
}

Deno.test("0234 Palindrom Linked List", () => {
  const test_cases: [number[], boolean][] = [
    [[1, 2, 2, 1], true],
    [[1, 2, 3, 2, 1], true],
    [[1, 2], false],
    [[1], true],
  ];

  for (let i = 0; i < test_cases.length; i += 1) {
    const test_case = test_cases[i];

    const head = array_to_linked_list(test_case[0]);
    const expected = test_case[1];

    const actual = is_palindrome(head);
    assertEquals(actual, expected, `test case: ${i}`);
  }
});
