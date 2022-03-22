# 银联-02. 优惠活动系统
# https://leetcode-cn.com/contest/cnunionpay-2022spring/problems/kDPV0f/
from typing import List
from collections import defaultdict
from collections import deque
from math import inf
import bisect
import heapq
'''
@File : 2.py
@Time : 2022/03/17 22:18:03
@Author : YuMin Zhang
@State : Indepeedent | Half-Depedent | Depedent 
@Thinking :
@Tag : Easy | Medium | Hard
'''
class Act:
    def __init__(self, actId, price, dis, num, useL):
        self.actId = actId
        self.price = price
        self.dis = dis
        self.num = num
        self.useL = useL
    
    def check(self, cost, user):
    
        if cost < self.price:
            return False
        # print(user.act[self.actId], self.useL)
        if user.act[self.actId] >= self.useL:
            return False
        if self.num <= 0:
            return False
        return True
        
class User:
    def __init__(self):
        self.act = defaultdict(int)
    
    def joinAct(self, actId):
        self.act[actId] += 1
        
    
        
class DiscountSystem:

    def __init__(self):
        self.users = defaultdict(User)
        self.acts = defaultdict(Act)
        


    def addActivity(self, actId: int, priceLimit: int, discount: int, number: int, userLimit: int) -> None:
        act = Act(actId, priceLimit, discount, number, userLimit)
        self.acts[actId] =act

    def removeActivity(self, actId: int) -> None:
        del self.acts[actId]


    def consume(self, userId: int, cost: int) -> int:
        if userId not in self.users:
            self.users[userId] = User()
        max_act_id = -1
        max_cost = 0
        # print("userId", userId)
        for act in self.acts.values():
            if act.check(cost, self.users[userId]):
                # print(act.actId, act.num)
                if act.dis > max_cost or (act.dis == max_cost and act.actId < max_act_id):
                    max_cost = act.dis
                    max_act_id = act.actId
        if max_act_id != -1:
            self.users[userId].joinAct(max_act_id)
            self.acts[max_act_id].num -= 1
        return cost - max_cost



# Your DiscountSystem object will be instantiated and called as such:
# obj = DiscountSystem()
# obj.addActivity(actId,priceLimit,discount,number,userLimit)
# obj.removeActivity(actId)
# param_3 = obj.consume(userId,cost)