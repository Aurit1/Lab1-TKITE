def printTopMost(dic:dict, n:int) -> None:
  try:
    sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    for i in range(n):
      print(sorted_dic[i][0].ljust(20) + str(sorted_dic[i][1]).rjust(5))
    return None
  except:
    return None

def countWords(list: list[str], Stopwords: list[str]) -> dict:
  dic = {}
  for string in list:
    if string in Stopwords: continue
    try:
      dic[string]  #Does the word exist in the dictionary already?
    except:
      dic.setdefault(string,0)  #If not, add it
    
    dic[string] += 1
  return dic

def tokenize(lines:list[str]) -> list:
  output = []  #Variable with the result inside
  for line in lines:  #Search through each line
    for word in line.split(): #Search through each word in the line
      numbers = ""  #Numbers when split from a numbers+letters combo gets put here
      letters = ""  #Letters when split from a numbers+letters combo gets put here
      special = ""  #Special characters are stored here
      for letter in word.lower(): #Goes through each letter in the words
        if not letter.isalpha(): #Checks if the letter isn't in the alphabet
          if not letter.isdigit():  #If a special character exists. Save it in a variable to append later
            if len(letters):          #
              output.append(letters)  #
              output.append(letter)   #
              letters = ""            #
              continue                #
            elif len(numbers):        #     If there are prior characters in the "word" append those characters i.e example! 
              output.append(numbers)  #     will append 'example' first and '!' second.
              output.append(letter)   #     if there aren't any characters before, it will append the special character
              numbers = ""            #     first i.e '"Room' will append '"' first and 'Room' second.
              continue                #
            else:                     #
              output.append(letter)   #
          else: #If it's not a special character it's a number
            numbers += letter
            continue
        else: letters += letter
      if len(numbers): output.append(numbers) #Append to output variable
      if len(letters): output.append(letters) # ^
      if len(special): output.append(special) #Special characters are a word of their own
  return output #Output