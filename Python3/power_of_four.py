class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0: return False
        
        while num > 1:
            if num % 4: return False
            num //= 4
            
        return True
