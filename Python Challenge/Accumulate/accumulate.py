def accumulate(collection, operation):
    
    for i in range(0, len(collection)):
        collection[i] = operation(collection[i])
    
    return collection