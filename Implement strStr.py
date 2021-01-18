class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def calShiftMat(st):
            dic = {}
            for i in range (len(st)-1,-1,-1):
                if not dic.get(st[i]):
                    dic[st[i]] = len(st)-i
            dic["ot"] = len(st)+1
            return dic
        if len(needle) > len(haystack):
            return -1
        if needle=="":
            return 0
        dic = calShiftMat(needle)
        idx = 0
        while idx+len(needle) <= len(haystack):
            str_cut = haystack[idx:idx+len(needle)]
            if str_cut == needle:
                return idx
            else:
                if idx+len(needle) < len(haystack):
                    cur_c = haystack[idx+len(needle)]
                    if dic.get(cur_c):
                        idx += dic[cur_c]
                    else:
                        idx +=dic["ot"]
                else:
                    return -1
        return -1 