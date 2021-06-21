# 1600. 皇位继承顺序
# https://leetcode-cn.com/problems/throne-inheritance/
from collections import defaultdict
from typing import List
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.heri_map = defaultdict(list)
        self.death_map = defaultdict(bool)


    def birth(self, parentName: str, childName: str) -> None:
        self.heri_map[parentName].append(childName)

    def death(self, name: str) -> None:
        self.death_map[name] = True

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def recursion(parentName):
            childs =  self.heri_map[parentName]
            if parentName not in self.death_map:
                ans.append(parentName)
            for child in childs:
                recursion(child)
        recursion(self.kingName)
        return ans





# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()