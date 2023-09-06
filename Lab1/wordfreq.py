""" stopwords = []
for line in open('./stopwords.txt').readlines():
  stopwords.append(line.replace('\n',''))
print(stopwords)
 """
def word_index(string: str) -> dict:
  dic = {}
  for s in string.split(): #Check each word in the string
    try:
      dic[s]  #Does the word exist in the dictionary already?
    except:
      dic.setdefault(s,[])  #If not, add it
    
    if string.split().index(s) in dic[s]:   #Check if the index of the word has already been inputed by another instance of the word
      dic[s].append(string.split().index(s,dic[s][len(dic[s])-1]+1))  #Add next index
    else:
      dic[s].append(string.split().index(s))
  return dic

characters = "1234567890!?.,:;()-&$"
print('1' in characters)
document = ['"They had 16 rolls of duct tape, 2 bags of clothes pins,',
           '130 hampsters from the cancer labs down the hall, and',
           'at least 500 pounds of grape jello and unknown amounts of chopped liver"',
           'said the source on a recent Geraldo interview.']

def tokenize(list:list) -> list:
  output = []
  for line in list:
    for word in line.split():
      pass