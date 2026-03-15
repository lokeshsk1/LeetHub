class Solution:
    def lastRemaining(self, n: int) -> int:
        
        step = 1
        head = 1
        left = True
        
        while n != 1:

            # print(n, head, step, left)

            if left:
                head += step
            else:
                if n%2!=0:
                    head += step

            step *= 2
            n //= 2
            left = not left

        return head



        # 2 4 6 8 10 12 14 16 20 22 24 26 28 30
        # 2 6 10 14 18 22 26 30
        # 2 10 18 26

