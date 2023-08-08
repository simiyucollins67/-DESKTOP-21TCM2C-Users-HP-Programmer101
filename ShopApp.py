print()
print('Welcome to Collins and Mariana Shop')
print()
print('This is my shopping list')
while True:
    print('1. Add item')
    print('2. Add another product')
    print('3. compute total')
    print('4. Thank you for shopping with us')
    print('5. quit application')
    print('please print one of these options:')
    print()
    select = int(input('please select a number to proceed:'))
    print()
    if select ==1:
        item=input('what would you like to add in your shopping list: ')
        price=int(input('type in the price: '))
        print (f'the price of your {item} is {price}') 
        continue
    elif select ==2:
        item_1=input('what would you like to add in your shopping list: ')
        price_1=int(input('type in the price: '))
        print (f'the price of your {item_1} is {price_1}')
        continue
    elif select ==3:
        total=price + price_1
        print(f"Please pay a total of {total} shillings")
        print("Thank you for shopping with us")

    elif select==4:
        print("Thank you for visiting our shop")
        print("We would love to see you again")
    break