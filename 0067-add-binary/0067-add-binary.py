class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binA = int(a,2) #이진수를 변환
        binB = int(b,2)
        
        print(binA, binB)
        
        sum = binA+ binB
        return bin(sum).split("0b")[1]