class Solution:
    def subs(self, inp, out, sub):
        if len(inp) == 0:
            sub.append(out)
        else:
            self.subs(inp[1:], out, sub)
            self.subs(inp[1:], out + [inp[0]], sub)
        return sub
    def subsets(self, A):
        return sorted(self.subs(A, [], []))
