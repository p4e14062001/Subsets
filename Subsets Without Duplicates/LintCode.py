class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subset(self, inp, out, ans):
        if len(inp) == 0:
            ans.append(out)
        else:
            self.subset(inp[1:], out, ans)
            self.subset(inp[1:], out + [inp[0]], ans)
        return ans
    def subsets(self, nums):
        return sorted(self.subset(sorted(nums), [], []))
