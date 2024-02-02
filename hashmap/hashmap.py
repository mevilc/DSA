# quick hashmap (dictionary) excercise

hashmap = {"A" : 10, "B" : 5}
for i in hashmap:
    print(f"{i} : {hashmap[i]}")

hash_map = dict()
for i in range(10):
    hash_map[i] = [ str(i), str(i + 1) ]

for i in hash_map:
    print(f"{i} : {hash_map[i]}")
