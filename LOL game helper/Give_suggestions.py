from gethtml import *
from findtop5 import *
from findrest import *
opggtohtml()
library = gettopfive()
print('Here are top 5 champions.')
for each in library:
    print('Champion:',each['name'], ',','Win rate:', each['winrate'], ',', 'KDA:', each['kda'], ',','Gold:', each['gold'])
ans = input('Do you want rest of the stats?')
if(ans == 'y'):
    rest = getrest()
    for it in rest:
        print('Champion:',it['name'], ',','Win rate:', it['winrate'], ',', 'KDA:', it['kda'], ',','Gold:', it['gold'])
