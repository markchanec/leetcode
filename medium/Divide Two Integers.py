def result(dividend, divisor): 
    min_m, multiple, max_m = 0, int(dividend/2), dividend

    while True:
        total = multiple*divisor
        tolerance = total - dividend

        if abs(tolerance) <= divisor:
            if tolerance > 0:
                multiple -=1
            if tolerance < 0 and tolerance ==divisor:
                multiple +=1
            break
        elif total < dividend: #low
            temp = multiple
            multiple = int((max_m - multiple)/2) + multiple
            min_m = temp
            
        elif total >dividend: #high
            temp = multiple
            multiple = int((multiple - min_m)/2) + min_m
            max_m = temp

    return multiple

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        multiple = 1

        if abs_divisor == 1:
            multiple = abs_dividend
        else:    
            multiple = result(abs_dividend, abs_divisor)

        if dividend <0 and divisor >0:
            multiple *= -1
        if dividend >0 and divisor <0:
            multiple *= -1

        if multiple <-2**31:
            multiple = -2**31
        elif multiple > 2**31-1:
            multiple = 2**31-1

        return multiple
