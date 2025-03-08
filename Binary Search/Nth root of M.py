#User function Template for python3

class Solution:
	def nthRoot(self, n: int, m: int) -> int:
	    
	    if n == 1: return m
		left, right = 0, m//n
		
		while left <= right:
		    
		    mid = (left+right)//2
			val = mid**n
		    
		    if val == m:
		        return mid
		    
		    elif val > m:
		        right = mid - 1
		    
		    else:
		        left = mid + 1
		 
		return -1
		        
