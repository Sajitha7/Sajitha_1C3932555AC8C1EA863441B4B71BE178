# Program = Product Search
def linear_search_product(product_list, target_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)
    return indices

# Provide a list of available products
available_products = ["apple", "banana", "orange", "apple", "grape", "apple"]

# Print the available products
print("Available products:", available_products)

# Ask the user for the target product
target_product = input("Enter the target product: ")

# Perform the linear search and get the indices
result = linear_search_product(available_products, target_product)

if result:
    print(f"The product '{target_product}' was found at indices: {result}")
else:
    print(f"The product '{target_product}' was not found.")