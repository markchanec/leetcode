class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        while True:
            if num>=1000:
                num-=1000
                s += "M"
            elif num>=900:
                num-=900
                s += "CM"
            elif num>=500:
                num-=500
                s += "D"
            elif num>=400:
                num-=400
                s += "CD"
            elif num>=100:
                num-=100
                s += "C"
            elif num>=90:
                num-=90
                s += "XC"
            elif num>=50:
                num-=50
                s += "L"
            elif num>=40:
                num-=40
                s += "XL"
            elif num>=10:
                num-=10
                s += "X"
            elif num>=9:
                num-=9
                s += "IX"
            elif num>=5:
                num-=5
                s += "V"
            elif num>=4:
                num-=4
                s += "IV"
            elif num>=1:
                num-=1
                s += "I"        

            if num == 0:
                break
        return s