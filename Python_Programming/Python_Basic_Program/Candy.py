class Solution:
    def candy(self, ratings):
        candy=0
        for i in range(len(rating)):
            if rating[i]==0:
                candy+=1
            else:
                candy+=rating[i]+1
        return candy
    
obj=Solution()
rating=[1, 0, 2]
candies=obj.candy(rating)
print(candies)