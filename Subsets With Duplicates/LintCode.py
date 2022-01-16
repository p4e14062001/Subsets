class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsets(self, inp, out, ans):
        ans.append(out)
        for i in range(len(inp)):
            if i > 0 and inp[i - 1] == inp[i]:
                continue
            self.subsets(inp[i+1:], out + [inp[i]], ans)
        return ans
    def subsetsWithDup(self, nums):
        return sorted(self.subsets(sorted(nums), [], []))
