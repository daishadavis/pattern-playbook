import typing


def lengthOfLongestSubstring(s: str) -> int:
    l = res = 0
    seen = set()

    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1

        seen.add(s[r])
        res = max(res, r - l + 1)

    return res


print(lengthOfLongestSubstring("zxyzxyz"))
