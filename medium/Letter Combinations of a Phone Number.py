def mapDigits(s):
    if s == "2":
        return "abc"
    elif s == "3":
        return "def"
    elif s == "4":
        return "ghi"
    elif s == "5":
        return "jkl"
    elif s == "6":
        return "mno"
    elif s == "7":
        return "pqrs"
    elif s == "8":
        return "tuv"
    elif s == "9":
        return "wxyz"
    
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combi = []
        letters = []

        for i in range(len(digits)):
            combi.append(mapDigits(digits[i]))

        digits = len(combi)
        #split 1st digit
        if digits > 0:
            for i in range(len(combi[0])):
                letters.append(combi[0][i])

        #split second digit
        if digits > 1:
            temp = letters
            letters = []
            for i in range(len(temp)):
                for j in range(len(combi[1])):
                    letters.append(temp[i] + combi[1][j])

        #split third digit
        if digits > 2:
            temp = letters
            letters = []
            for i in range(len(temp)):
                for j in range(len(combi[2])):
                    letters.append(temp[i] + combi[2][j])

        #split fourth digit
        if digits > 3:
            temp = letters
            letters = []
            for i in range(len(temp)):
                for j in range(len(combi[3])):
                    letters.append(temp[i] + combi[3][j])

        return letters