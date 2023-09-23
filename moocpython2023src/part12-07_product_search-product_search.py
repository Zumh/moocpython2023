# Write your solution here

def search(products: list, criterion: callable)->list:
    """
    The second argument to the function is a function itself, and it should be able to process a tuple as defined above, and return a Boolean value. 
    The search function should return a new list containing those tuples from the original which fulfil the criterion.
    """
    return [product for product in products if criterion(product)]

def price_under_4_euros(product):
    return product[1] < 4

if __name__ == "__main__":
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22), ("kale", 0.99, 1)]
    for product in search(products, price_under_4_euros):
        print(product)