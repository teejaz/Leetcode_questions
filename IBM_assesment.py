#Input: words = ["aba","aabb","abcd","bac","aabc"]
#Output: 2
#Explanation: There are 2 pairs that satisfy the conditions:
#- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
#- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'. 

count = 0
for i in range(len(words)):
  for j in range(i):
    if set(words[i]) == set(words[j]):
      count += 1

return count

  
