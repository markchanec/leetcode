class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        i=0

        while i<len(s):
            if s[i] == "I":
                if i+1<=len(s)-1:
                    if s[i+1] == "V":
                        sum+=4
                        i+=1
                    elif s[i+1] == "X":
                        sum+=9
                        i+=1
                    else:
                        sum+=1
                else:
                    sum+=1
            elif s[i] == "V":
                sum+=5
            elif s[i] == "X":
                if i+1<=len(s)-1:
                    if s[i+1] == "L":
                        sum+=40
                        i+=1
                    elif s[i+1] == "C":
                        sum+=90
                        i+=1
                    else:
                        sum+=10
                else:
                    sum+=10
            elif s[i] == "L":
                sum+=50
            elif s[i] == "C":
                if i+1<=len(s)-1:
                    if s[i+1] == "D":
                        sum+=400
                        i+=1
                    elif s[i+1] == "M":
                        sum+=900
                        i+=1
                    else:
                        sum+=100
                else:
                    sum+=100
            elif s[i] == "D":
                sum+=500
            elif s[i] == "M":
                sum+=1000
            i+=1
    #         print(sum)
        return sum
