class Solution:
    def subset(self, inp, out, ans):
        if len(inp) == 0:
            ans.append(out)
        else:
            self.subset(inp[1:], out, ans)
            self.subset(inp[1:], out + [inp[0]], ans)
        return ans
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subset(nums, [], [])
