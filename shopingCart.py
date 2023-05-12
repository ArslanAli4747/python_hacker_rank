#!/bin/python3

import math
import os
import random
import re
import sys



class Item:
    # Implement the Item here
    def __init__(self,name:str,price:int):
        self.name = name
        self.price = price


class ShoppingCart:
     # Implement the ShoppingCart here
    def __init__(self):
        self.cart = []
    def add(self,item:Item):
        self.cart.append(item)
    def total(self)->int:
        # return sum of all items in the cart
        sum_of_items = 0
        for item in self.cart:
            sum_of_items+=item.price
        return sum_of_items
    def __len__(self):
        return len(self.cart)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
            
    fptr.close()
