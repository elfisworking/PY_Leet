from typing import List
class Solution:
    # 采用深度遍历的方法
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        phoneMap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxzy"
        }
        def backrtack(index:int):
            if index == len(digits):
                conbinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backrtack(index+1)
                    combination.pop()
        
        combination = list()
        conbinations = list()
        backrtack(0)
        return conbinations
s = Solution()
print(s.letterCombinations("23"))