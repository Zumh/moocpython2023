# write your solution here

def read_fruits():
    fruits_name_price = {}
    with open("fruits.csv") as fruits:
        for fruit in fruits:
            fruit = fruit.replace("\n","")
            fruit_datas = fruit.split(";")
            fruits_name_price[fruit_datas[0]] = float(fruit_datas[1])
        

    return(fruits_name_price)
