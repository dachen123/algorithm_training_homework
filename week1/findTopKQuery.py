#训练场题目：数据流查询
#思路：1.先将指令集按照queryID排序
#     2.对每个指令生成一个K长度的执行时间序列
#     3.使用一个大小与指令数量相等的堆进行对步骤2得出的时间序列进行k次堆排序
class Solution:
    def findTopKQuery(self, orders: List[List[int]], k: int) -> List[int]:
        orders = sorted(orders,key=lambda x:x[0])
        heap = []
        import heapq
        orders_exec_time = [None for i in range(len(orders))]
        for i in range(len(orders)):
            orders_exec_time[i] = []
            for o in range(k):
                orders_exec_time[i].append([orders[i][1]+o*orders[i][2]])

        for i in range(len(orders_exec_time)):
            heapq.heappush(heap,(orders_exec_time[i][0],i))
            
            orders_exec_time[i].pop(0)
        result = []
        while heap:
            exec_time,idx = heapq.heappop(heap)
            result.append(orders[idx][0])
            if len(result)==k:
                return result
            if orders_exec_time[idx]:
                heapq.heappush(heap,(orders_exec_time[idx][0],idx))
                orders_exec_time[idx].pop(0)
        return result
             
            
