from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        l = len(coordinates)
        if l<=2 :
            return True
        dot_one = coordinates[0]
        dot_two = coordinates[1]
        if dot_one[0] == dot_two[0]:
            for i in range(2,l):
                dot = coordinates[i]
                if dot[0] != dot_one[0]:
                    return False
        else:
            k = (dot_one[1]-dot_two[1])/(dot_one[0]-dot_two[0])
            for i in range(2,l):
                dot = coordinates[i]
                if dot[1] != k*(dot[0]-dot_one[0])+dot_one[1]:
                    return False
        return True

s = Solution()
print(s.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))