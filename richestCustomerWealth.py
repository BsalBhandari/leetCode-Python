class Solution(object):
    def maximumWealth(self, acc : list[list[int]]) -> int:
        
        '''
        acc has a list inside a list. so we use two loops to figure out the richest customer.
        the first loop iterate us the customer account which is stored in i(bank accounts)
        the second loop iterate the money on the account and the total amount is stored in customer_money.
        finally it it appended to list named money and
        finally max method is used to figure out the richest person.
        
        '''

        money =[]
        for i in acc:
            customer_money = 0
            for j in i:
                customer_money += j
            money.append(customer_money)
        return max(money)

test1= Solution()
print(test1.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))

'''
acc : [[2,8,7],[7,1,3],[1,9,5]]

output : 17
'''
