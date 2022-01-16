class Solution:
    def subset(self, inp, out, ans):
        ans.append(out)
        for i in range(len(inp)):
            if i > 0 and inp[i - 1] == inp[i]:
                continue
            self.subset(inp[i+1:], out + [inp[i]], ans)
        return ans
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        return sorted(self.subset(sorted(nums), [], []))
