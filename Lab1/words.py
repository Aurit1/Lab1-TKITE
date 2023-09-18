def words(s):
    start = 0
    while start < len(s):
        while start < len(s) and s[start].isspace():
            start += 1
        
        end = start
        while end < len(s) and not s[end].isspace():
            end += 1
        
        print(s[start:end])
        
        start = end
        
words("I ate twelve chickens")