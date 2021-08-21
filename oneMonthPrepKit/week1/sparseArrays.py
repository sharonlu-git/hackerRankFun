def matchingStrings(strings, queries):
    # Write your code here
    queryList = []
    for query in queries:
        queryList.append(strings.count(query))
        
    return queryList
