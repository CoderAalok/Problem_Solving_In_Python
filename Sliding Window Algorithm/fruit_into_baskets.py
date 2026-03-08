def fruit_into_baskets(nums) :
    low, res = 0, -1
    big_basket = {}
    for high in range(len(nums)):
        big_basket[nums[high]] = big_basket.get(nums[high],0) + 1
        while len(big_basket) > 2:
            #shrink low
            big_basket[nums[low]] -= 1
            if big_basket[nums[low]] == 0:
                del big_basket[nums[low]]
            low += 1
        
        size = high-low+1
        res = max(res, size)
    
    return res

nums = [1,1,0,2,2,4,3,3,3,1,1,1]
print(fruit_into_baskets(nums))
