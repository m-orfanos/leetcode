import { assertEquals } from "https://deno.land/std@0.224.0/assert/assert_equals.ts";

function longest_palindrome(s: string): number {
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
        const actual = longest_palindrome(s);

        assertEquals(actual, expected, `failed soln#1 for n=${s}`);
    }
});
