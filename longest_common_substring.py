# longest common prefix 
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        self.strs = strs
        result = ""
        strs = strs.sort()
        self.first= self.strs[0]
        self.last = self.strs[len(self.strs)-1]

        for i in range(min(len(self.first),len(self.last))):
            if self.first[i] != self.last[i] :
                return result
            result = result+self.first[i]
        return result


strs = ["abbb","ab","abc","abvcd","abr"]
ob =Solution()
op=ob.longestCommonPrefix(strs)
print(op)
