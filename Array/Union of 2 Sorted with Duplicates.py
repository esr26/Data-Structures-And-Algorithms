class Solution:
    

    def findUnion(self,a,b):

        
        res = []
        i = j = 0
        n = len(a)
        m = len(b)
        
        while i < n and j < m:
            if res:
                if res[-1]==a[i] and res[-1] == b[j]:
                    i += 1
                    j += 1
                    continue
                    
                elif res[-1] == a[i]:
                    i += 1
                    continue
                elif res[-1]==b[j]:
                    j += 1
                    continue
                
                    
            if a[i] == b[j]:
                res.append(a[i])
                i+=1
                j += 1
            elif a[i] > b[j]:
                res.append(b[j])
                j += 1
                
            else:
                res.append(a[i])
                i += 1
               
        while i < n:
            if res[-1] != a[i]:
                res.append(a[i])
            
            i += 1
        
        while j < m:
            if res[-1] != b[j]:
                res.append(b[j])
            j+= 1
            
        return res
