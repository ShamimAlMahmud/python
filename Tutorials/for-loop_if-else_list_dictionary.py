game =[[0,0,0,],
      [0,0,1,],
      [0,0,2,], 'SHamim', 1, 5.4]

# print(game)
# print(game[0])
# print(type(game[5]))
# print(type(game))


# for shamim_al_mahmud in game:
#       print(shamim_al_mahmud)
#       print(type(shamim_al_mahmud))


for element in game:
      if type(element) is list:
            print(element)
      elif type(element) == int:
            print("this is an interger type")
      else:
            print("This is neither list or integer type")
      
for i in range(-1,10):
      print(i)
shamim = "Shamim is boy now"
print(shamim)



# Dictionary
dict2 = {
            "name": "Shamim",
            "genfer," : "boy",
            "Uni" : "BAIUST",
            "mobile_no" : "0123456"
       }
print(dict2, type(dict2))

print(dict2["name"],dict2["mobile_no"])

list1 = [shamim, [1, 2, 3]]
print(list1[0])

dict1 = {
      "name" : "Shamim"
}
print(dict1["name"])
print(dict2["name"],dict1["name"])


print(list1)
print(dict1)