#训练场题目：每日在线用户量
#思路：单调栈的应用

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        count = [0] * len(T)
        st = []
        for i in range(len(T)-1,-1,-1):
            while st and T[i] > T[st[-1]]:
                st.pop()
            count[i] = st[-1] -i  if st else 0
            st.append(i)
        return count
