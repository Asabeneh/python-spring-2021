
from pprint import pprint as pp
import re

# freq_table = {}
# with open('./melina_speech.txt') as f:
#    words = f.read().lower().split()
#    for word in words:
#        if word in freq_table:
#            freq_table[word] += 1
#        else:
#            freq_table[word] = 1
# pp(freq_table)



sentence = '''%I @$am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I@ found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher love JavaScript!?. I have teaching since 2016 and I enjoy the teaching upto now in 2021.'''

# SPECIAL CHARACTERS

pattern = r'[%@$&#,;\.!?0-9]+'

cleaned_txt = re.sub(pattern, '', sentence)
print(cleaned_txt)
words = cleaned_txt.split()
print(words)
print(len(words))
   

