def checkMagazine(magazine, note):
    # Dictionary Method
    dict1 = {}
    dict2 = {}
    for word in magazine:
        dict1.setdefault(word,0)
        dict1[word] += 1
    for word in note:
        dict2.setdefault(word,0)
        dict2[word] += 1
    for key,value in dict2.items():
        if key not in dict1 or dict1[key] < dict2[key]:
            print("No")
            return
    print("Yes")

