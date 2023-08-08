from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:

        dict={}

        temp_list=[]
        result=[0]*k
        for i in range(len(logs)):
            if logs[i][0] in dict:
                if logs[i][1] not in dict[logs[i][0]]:
                    dict[logs[i][0]].append(logs[i][1])
            else:
                dict[logs[i][0]]=[logs[i][1]]
        for i in dict:
            temp_list.append(len(dict[i]))
        for i in temp_list:
            result[i-1]+=1
            print(result)
        return result


logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
k = 5
solution = Solution()
solution.findingUsersActiveMinutes(logs, k)