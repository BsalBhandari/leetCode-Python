class Solution(object):
    def integerToRoman(self, num):
        roman_val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        roman_letters = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman= ""
        i =0
        while num >0:
            for _ in range(num // roman_val[i]):
                roman+= roman_letters[i]
                num -= roman_val[i]
            i+=1
        return roman

test1 = Solution()
test_val = test1.integerToRoman(1254)
print(test_val)

'''
input: 1254

output: MCCLIV
'''