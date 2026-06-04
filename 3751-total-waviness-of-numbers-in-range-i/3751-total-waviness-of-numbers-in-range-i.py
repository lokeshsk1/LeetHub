class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        waves = 0

        for i in range(num1, num2+1):
            for j in range(1, len(str(i))-1):
                if int(str(i)[j]) > int(str(i)[j-1]) and int(str(i)[j]) > int(str(i)[j+1]):
                    waves += 1
                if int(str(i)[j]) < int(str(i)[j-1]) and int(str(i)[j]) < int(str(i)[j+1]):
                    waves += 1
        return waves