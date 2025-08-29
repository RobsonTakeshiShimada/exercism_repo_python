def is_isogram(string):
    string = string.lower()
    for i in string:
        if string.count(i)>1 and i.isalpha():
            return False
    return True
        
