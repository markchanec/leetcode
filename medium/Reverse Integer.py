class Solution:
    def reverse(self, x: int) -> int:
        reverse_x = str(x)[::-1]
        if reverse_x[-1]=="-":
            reverse_x = reverse_x[:-1]
            x = int(reverse_x)
            x *= -1
        else:
            x = int(reverse_x)

        if x > 2**31-1 or x < -2**31:
            x = 0
        return x