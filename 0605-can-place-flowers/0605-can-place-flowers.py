class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        result = 0
        flowerbed_length = len(flowerbed)
        for i in range(flowerbed_length):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (i == flowerbed_length -1 or flowerbed[i+1] == 0):
                    result += 1
                    flowerbed[i] = 1

        if result >= n:
            return True
        else:
            return False