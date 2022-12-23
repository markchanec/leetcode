class Solution:
    def maximumSwap(self, num: int) -> int:
        lst = list(str(num))
        sorted_lst = sorted(lst, reverse=True)

        for i in range(len(sorted_lst)):
            if sorted_lst[i] > lst[i]:
                reverse_list = list(reversed(lst[i:]))
                index = len(lst) - reverse_list.index(sorted_lst[i]) -1
                lst[i], lst[index] = lst[index], lst[i]
                break;

        return "".join(lst)