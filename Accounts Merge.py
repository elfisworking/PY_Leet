from typing import List
import collections
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, index1: int, index2: int):
        self.parent[self.find(index2)] = self.find(index1)

    def find(self, index: int) -> int:
        if self.parent[index] != index:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToIndex = dict()
        emailToName = dict()

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in emailToIndex:
                    emailToIndex[email] = len(emailToIndex)
                    emailToName[email] = name
        
        uf = UnionFind(len(emailToIndex))
        # 将每一个用户先看作一个类  使用union将它们合并
        for account in accounts:
            firstIndex = emailToIndex[account[1]]
            for email in account[2:]:
                uf.union(firstIndex, emailToIndex[email])
        
        indexToEmails = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            index = uf.find(index)
            indexToEmails[index].append(email)
        
        ans = list()
        for emails in indexToEmails.values():
            ans.append([emailToName[emails[0]]] + sorted(emails))
        return ans


    # def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    #     dic = {}
    #     name = {}
    #     for id ,account in enumerate(accounts):
    #         flag = False
    #         father = -1
    #         for i in range(1,len(account)):
    #             mail = account[i]
    #             if mail in account[:i]:
    #                 continue
    #             if mail  in dic :
    #                 flag = True
    #                 father=dic[mail]
    #                 break
    #             else:
    #                  dic[mail] =id
    #         if flag :
    #             for i in range(1,len(account)):
    #                 dic[account[i]] =father
    #         else:
    #             name[id] = account[0]
    #     temp = {}
    #     for key , value in dic.items():
    #         if value in temp:
    #             l = temp[value]
    #             l.append(key)
    #             temp[value] = l
    #         else:
    #             temp[value] = [key]
    #     ans = []
    #     for key , value in temp.items():
    #         value.sort()
    #         ans.append([name[key]]+value)
    #     return ans
s = Solution()
print(s.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]))
        
                
         
            
