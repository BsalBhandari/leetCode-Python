class Romantointeger():
    def romanToInteger(self,  input: str) -> int:
        
        roman = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000} # creating a dictionary to get equivalent value for their corresponding roman letters

        res = 0 

        for i in range(len(input)):
            if i +1 < len(input) and roman[input[i]] < roman[input[i+1]]: 
                res -= roman[input[i]]
            else:
                res += roman[input[i]]
        return res

integer = Romantointeger()
print(integer.romanToInteger("LVIII"))

'''
Case I
Input = LVIII

Output = 58

Case II
Input = XI
 
Output = 9

'''