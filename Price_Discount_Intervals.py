# Code calculates price discounts with a given price and discount intervals

# Results will return the Original Price and Discounted Price

Price = 100
Discount_Intervals = [50, 100, 200]
Discounts = [0, 0.1, 0.2, 0.25]

print("The original price is {}".format(Price))

if Price < Discount_Intervals[0]:
    Price = Price * (1-Discounts[0])
elif Price < Discount_Intervals[1]:
    Price = Price * (1-Discounts[1])
elif Price < Discount_Intervals[2]:
    Price = Price * (1-Discounts[2])
else:
    Price = Price * (1-Discounts[3])

print("And the after discount price is {}!".format(Price))