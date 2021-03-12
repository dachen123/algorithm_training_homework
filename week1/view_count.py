#训练场题目3 视野总和
#思路：用了单调栈的方式进行处理
class Solution:
    def fieldSum(self, v: List[int]) -> int:
        count = [0 for i in range(len(v))]
        st = []
        for i in range(len(v)-1,-1,-1):
            while st and v[i] > v[st[-1]]:
                st.pop()
            
            count[i] = st[-1] - i-1 if st else len(v)-1 -i
            
            st.append(i)
        return sum(count )
