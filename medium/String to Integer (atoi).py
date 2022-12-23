class Solution:
    def myAtoi(self, s: str) -> int:
        neg = False
        substring = ""

        for i in range(len(s)):
            if s[i]==" ":
                if substring!="":
                    break
                continue
            elif s[i]=="0" and substring=="":
                substring += s[i]
            elif s[i]=="-" and substring=="":
                if i+1<len(s):
                    if not s[i+1].isdigit():
                        break
                neg = True
                continue
            elif s[i]=="+" and substring=="":
                if i+1<len(s):
                    if not s[i+1].isdigit():
                        break
                continue
            elif s[i].isdigit():
                substring += s[i]
            else:
                break

        if substring == "":
            substring = "0"

        result = int(substring)
        if neg:
            result = result*-1


        if result <-2**31:
            result = -2**31
        elif result > 2**31-1:
            result = 2**31-1

        return result