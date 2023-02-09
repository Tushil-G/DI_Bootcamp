# Word = input("Enter a word please: ") 
# index = {}
# for i, x in enumerate(Word): 
#     print(f"At position {i}, we have the letter {x}")
#     if i in index.keys(): 
#         index[i].append(x) 
#     else: 
#         index[x] = [i]

# print(index)
#excercise 2
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}
wallet=input("enter the amount of money you have: ")
cash=int(wallet.replace("$",""))
affordable=[]

for key,value in items_purchase.items():
    print(key,"--", value)
    price=value.replace("$","")
    price=price.replace(",","")
    price_int=int(price)
    if cash>=price_int:
        affordable.append(key)
    else:
        print("you broke")
        
print(sorted(affordable))
     