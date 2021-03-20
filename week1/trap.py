#接雨水
#暴力方案
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        w_sum = 0
        for i in range(1,len(height)-1):
            left_max = 0
            for l in range(i,-1,-1): #若从i+1开始遍历，则求的left_max可能比height[i]小，min(left_max,right_max) - height[i] 需要和0比取较大值
                left_max = max(left_max,height[l])
            right_max = 0
            for r in range(i,len(height)): #若从i+1开始遍历，则求的right_max可能比height[i]小，min(left_max,right_max) - height[i] 需要和0比取较大值
                right_max = max(right_max,height[r])
            w_sum += min(left_max,right_max) - height[i]   
        return w_sum

#动态编程方案
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        w_sum = 0
        left_max = [0] * len(height)
        left_max[0] = height[0]
        right_max = [0] * len(height)
        right_max[-1] = height[-1]
        for i in range(1,len(height)-1):
            left_max[i] = max(height[i],left_max[i-1])
        for i in range(len(height)-2,0,-1):
            right_max[i] = max(height[i],right_max[i+1])
        for i in range(1,len(height)-1):
            w_sum += min(left_max[i],right_max[i]) - height[i]
        return w_sum
#单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        w_sum = 0
        st = []
        for i in range(0,len(height)):
            while st and height[i] > height[st[-1]]:
                top = st.pop()
                if not st:
                    break
                distance = i - st[-1] -1
                w_height = min(height[i],height[st[-1]]) - height[top]
                w_sum += distance * w_height
            st.append(i)
        return w_sum
#双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        w_sum = 0
        left,right = 0,len(height)-1
        left_max,right_max = height[0],height[-1]
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max: #在左指针值小于右指针值条件下，left_max即为左边界，left_max-height[left]即为雨水深度
                    left_max = height[left]
                else:
                    w_sum += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    w_sum += right_max - height[right]
                right -= 1
        return w_sum