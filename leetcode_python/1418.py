# 1418. 点菜展示表
# https://leetcode-cn.com/problems/display-table-of-food-orders-in-a-restaurant/
from typing import List
from collections import defaultdict
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = defaultdict(lambda:defaultdict(int))
        foods = set()
        tables = set()

        for order in orders:
            n = int(order[1])
            table = d[n]
            table[order[2]] += 1
            foods.add(order[2])
            tables.add(n)
        
        ans = []
        foods = list(foods)
        foods.sort()
        ans.append(["Table"]+foods)
        tables = list(tables)
        tables.sort()
        
        for table in tables:
            tmp = [table]
            t = d[table]
            for food in foods:
                if food not in t:
                    tmp.append("0")
                else:
                    tmp.append(str(t[food]))
            ans.append(tmp)

        return ans 

s = Solution()
print(s.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
