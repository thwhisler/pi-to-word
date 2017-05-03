#turn the decimals of pi into a ascii characters semi arbitraly, maybe find words
import string

f = open('pi.txt', 'r')
pi = f.read()
pi = pi.replace(' ','')
#print(pi)
f.close()
i = 0
charlist = ''
while i+3 < len(pi):
    char1 = pi[i]
    char2 = pi[i+1]
    char3 = pi[i+2]
    
    #grab 3 digits instead if it will be 100-126
    #this arbitraily disincludes 0-26 but we can't print those anyway
    temp = (int(char1+char2+char3))
    if temp > 126:
        temp = (int(char1+char2))
        i += 2
    else:
                i += 3
    #discounting non printable characters
    #if int(temp) > 32:
    #discounting non letters
    if (temp >= 65 and temp <= 90) or (temp >= 97 and temp <= 122):
        temp = chr(temp)
        charlist = charlist + temp

#print(charlist)    
f = open('piletters.txt', 'w')
f.write(charlist)
f.close()
