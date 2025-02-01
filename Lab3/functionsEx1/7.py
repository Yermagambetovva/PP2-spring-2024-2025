def has_33(nums):
    for i in range(len(nums) - 1):  #prohoditsa po spusku do predposlednego elementa
        if nums[i] == 3 and nums[i + 1] == 3:  #proveraet est li dva podryat idushih 3
            return True
    return False  #esli net ni odnloi pary 3 to False

print(has_33([1, 3, 3]))      #True
print(has_33([1, 3, 1, 3]))   #False
print(has_33([3, 1, 3]))      #False
