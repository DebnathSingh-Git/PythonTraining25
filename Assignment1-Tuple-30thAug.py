# Create a tuple named product containing the following items: "Laptop", 50000, Black ,'Samsung' and "Electronics". Print the tuple.
product = ("Laptop", 50000, 'Black' ,'Samsung', "Electronics")
print("product: ", product)
 
# Access and print the second element of the tuple product.
print("product 2nd Element: ", product[1])
 
# Slice and print the last two elements of the product tuple.
print("Slice and print the last two elements: ", product[-2:])

# Check whether "Electronics" is present in the product tuple and print a message.
if "Electronics" in product:
    print("Electronics is present") 
 
# Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900). Count how many times 1000 appears.
prices =  (1000, 1500, 1200, 1100, 900)
print("times 1000 appears: ", prices.count(1000))
 
# Find and print the maximum and minimum price from the prices tuple.
print ("Max:", max(prices), "  Min: ", min(prices))
 
# Use a loop to print each item from the product tuple on a new line.
for item in product:
    print("Item: ", item)
 
# Convert the product tuple to a list. Change the price to 55000, then convert it back to a tuple. Print the updated tuple.
product_list = list(product)
product_list[1] = 55000
product = tuple(product_list)
print("Updated tuple: ", product)
 
# Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
# product_list = list(product)
# product_list.extend(["In Stock"])
# product = tuple(product_list)
product_list = ("In Stock",)
final_prod = product + product_list
print("Updated tuple after new item In Stock: ", final_prod)
 
# Remove "Electronics" from the product tuple (by converting to list, removing, and converting back).
product_list2 = list(product)
product_list2.remove("Electronics")
product = tuple(product_list2)
print("Updated tuple after removing Electronics: ", product) 
 
# Unpack the tuple product into three variables and print each variable.
type, price, *rest = product
print("Type: ", type, " Price: ", price , "  rest: ", rest)
 
# Create a nested tuple that contains three product tuples inside it. Access and print the name of the second product in the nested tuple.
product2 = ("Mouse", 300, 'Black' ,'HP', "Electronics")
product3 = ("Keyborad", 200, 'Black' ,'HO', "Electronics")
nestedtuple = (product, product2, product3)
print("2nd product: ", nestedtuple[1])

 