"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.
You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings).
Please reload the code definition to get the latest changes.

"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def is_valid(tmp_s):
            if not tmp_s:
                return True
            for i in xrange(len(tmp_s)):
                if tmp_s[:i+1] in wordDict and is_valid(tmp_s[i+1:]):
                    return True
            return False

        return is_valid(s)

if __name__ == "__main__":
    assert Solution().wordBreak("leetcode", ["leet", "code"]) is True
