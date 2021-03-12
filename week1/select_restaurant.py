#训练场题目：选择餐馆
# 思路：先筛选符合条件的餐馆，再进行排序
# 疑问：关于排序用了python 的sorted方法，不知道这里有没有更好的方式处理?
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], filters: List[int]) -> List[int]:
        valid_restaurants= []
        for r in restaurants:
            if r[2] >= filters[0] and r[3] <= filters[1] and r[4] <= filters[2]:
                valid_restaurants.append(r)
        valid_restaurants = sorted(valid_restaurants,key=lambda x:(x[1],x[0]),reverse=True)
        res = [r[0] for r in valid_restaurants]
        return res