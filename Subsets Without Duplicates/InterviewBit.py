class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def subset(self, inp, out, ans):
        if len(inp) == 0:
            ans.append(out)
        else:
            self.subset(inp[1:], out, ans)
            self.subset(inp[1:], out + [inp[0]], ans)
        return ans
	def subsets(self, A):
        return sorted(self.subset(sorted(A), [], []))
