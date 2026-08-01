class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        
        c = y // 4

        mn = min(x, c)

        print(mn)

        return "Alice" if mn % 2 else "Bob"