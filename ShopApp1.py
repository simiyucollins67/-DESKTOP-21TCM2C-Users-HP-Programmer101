class shopitems:
    def __init__(self, product_name, price, stockquantity, product_list): #Instantiate the objects in a class
        self.product_name = product_name
        self.price = price
        self.stockquantity = stockquantity
        self.product_list=product_list 
# pen =shopitems('bic', 5, 'blue')
# print(pen.product_name)
# print(pen.price)
# print(pen.stockquantity)
# print() 
        while True:
            option=(int(input("Please select an option to proceed: \n")))
            print("1. List of products in stock: ")
            print("2. Add new product to stock: ")
            print("3. Remove sold product from stock: ")
            print("4.  Update product list: ")
            print("5. Update product price: ")
            print("6. Exit application")
            print()
            print()            
        #print("You have not selected a viable option, please reselect")
            def product_list(self):
                   print(input("The products available are: "))           
            if option == 1: 
                    print("{product_name}", sep="\t ")
            else: 
                    print("Product not in list")







