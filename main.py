class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        decode = []
        
        for i in range(0, len(code)) :
            if k == 0 : 
                decode.append(0)
            
            if k > 0 :
                sum = 0
                
                for j in range(1, k + 1) :
                    if i + j < len(code) :
                        sum += code[i + j]
                    else :
                        sum += code[i + j - len(code)]
                
                decode.append(sum)
                sum = 0
            
            if k < 0 :
                sum = 0
                
                for j in range(-1, k - 1, -1) :
                    if i + j >= 0 :
                        sum += code[i + j]
                    else :
                        sum += code[len(code) + i + j]

                decode.append(sum)
                sum = 0
        
        return decode