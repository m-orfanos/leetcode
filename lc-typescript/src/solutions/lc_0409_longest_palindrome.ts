import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function longest_palindrome1(s: string): number {
    const counter: { [key: string]: number } = {};
    for (const ch of s) {
        counter[ch] = (counter[ch] || 0) + 1;
    }

    let has_odd = false;
    let ans = 0;
    for (const [_, cnt] of Object.entries(counter)) {
        let offset = 0;
        if (cnt % 2 == 1) {
            has_odd = true;
            offset = 1;
        }
        ans += (cnt - offset);
    }

    if (has_odd) {
        ans += 1;
    }

    return ans;
}

function longest_palindrome2(s: string): number {
    // alphabet both lower and uppercase letters
    // [A, B, C, ..., Z] -> [65, 66, 67, ..., 90]
    // [a, b, c, ..., z] -> [97, 98, 99, ..., 122]
    // use 2**7 = 128 because
    const histogram: number[] = [];
    for (let i = 0; i < 2 ** 7; i++) {
      histogram.push(0);
    }

    for (let j = 0; j < s.length; j++) {
      histogram[s.charCodeAt(j) - 65] += 1;
    }
  
    let hasOdd = false;
    let ans = 0;
    for (let k = 0; k < histogram.length; k++) {
      ans += 2 * Math.floor(histogram[k] / 2);
      hasOdd = hasOdd || histogram[k] % 2 === 1;
    }
  
    return ans + (hasOdd ? 1 : 0);
  }

Deno.test("0409 Longest Palindrome", () => {
    const test_cases: [string, number][] = [
        ["abccccdd", 7],
        ["a", 1],
        ["ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy", 867],
    ];

    for (let i = 0; i < test_cases.length; i += 1) {
        const test_case = test_cases[i];

        const s = test_case[0];

        const expected = test_case[1];

        const actual1 = longest_palindrome1(s);
        assertEquals(actual1, expected, `failed soln#1 for n=${s}`);

        const actual2 = longest_palindrome2(s);
        assertEquals(actual2, expected, `failed soln#1 for n=${s}`);
    }
});
