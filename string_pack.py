# __author__ = Dejan Djokic            
# __mentor__ = Patricia Francis-Lyon
# __date__ = 10/29/2013             
# __course__ = Computer Science 110     
# __program__ = stringPack               
# __email__ = "ddjokic@dons.usfca.edu" 
#-------------------------------------
# stringPack is a set of algorithms, mostly designed for strings. 
#The following functions operate with strings for their easier utilization.

# Returns the number of occurrences of character c in string s.

def numOccur(s, c):
    """
    >>> numOccur('missisippi', 'i')
    4
    >>> numOccur('','d')
    0
    >>> numOccur('zzzzzzzzzzzzzzzzzzzzzz', 'z')
    22
    >>> numOccur('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'f')
    0
    >>> numOccur('dkjasldsklasadkljjskdajskadjklasdAASDASDSDAddsa', 'A')
    4
    >>> numOccur('iloveprogramming', 'i')
    2
    >>> numOccur('nemadanaadanemislimnatebe', 'a')
    6
    >>> numOccur('python231ddddddd_code', 'd')
    8
    >>> numOccur('sssssssssssdakndsaklskadjl         ', ' ')
    9
    >>> numOccur(' ', ' ')
    1
    
    """
    i = 0
    for char in s:
        if char == c:
            i += 1
    return i

# Returns the index of the last occurrence of character c in string s 
# or -1 if c does not occur in s. 

def lastOccur(s, c):
    """
    >>> lastOccur('hello', 'l')
    3
    >>> lastOccur('djokic', 'y')
    -1
    >>> lastOccur('playstation', 't')
    7
    >>> lastOccur('nicolascage', 'o')
    3
    >>> lastOccur('fafafafafafafa', 'a')
    13
    >>> lastOccur('asfddgghgjkl[ooiuugfhgm,jhgffdswertyioupicbvmnmmm', 'q')
    -1
    >>> lastOccur('doctestdoctest', 't')
    13
    >>> lastOccur('      ', ' ')
    5
    >>> lastOccur('samplesequenceofbusinessmajorcourses', 's')
    35
    >>> lastOccur('how does space work', ' ')
    14
    >>> lastOccur('final try', 'r')
    7
    """
    for i in range(len(s)-1, -1, -1):
       if s[i] == c:
           return i
    return -1

# Returns the index of the last occurrence of the character that most frequently occurs
# in string s or -1 if s is the empty string.

def lastOccurMostFreqChar(s):
    """
    >>> lastOccurMostFreqChar('asdfdfasadsaaaa')
    14
    >>> lastOccurMostFreqChar('jdsajdsaj')
    8
    >>> lastOccurMostFreqChar('    ')
    3
    >>> lastOccurMostFreqChar('zvezdamijesve')
    12
    >>> lastOccurMostFreqChar('')
    -1
    >>> lastOccurMostFreqChar('ddddddssssssssssssssdd')
    19
    >>> lastOccurMostFreqChar('')
    -1
    >>> lastOccurMostFreqChar('svakipredahjeluksuz')
    17
    >>> lastOccurMostFreqChar('uppers,downers,all-arounders')
    26
    >>> lastOccurMostFreqChar('microsoft')
    6
    >>> lastOccurMostFreqChar('victory')
    6
    """
    count_mf = 0
    elem_mf = -1
    for elem in range(len(s)):
        count = numOccur(s, s[elem])
        if count >= count_mf:
            count_mf = count
            elem_mf = elem
    return elem_mf

# Returns a new string that is equivalent to string s1 with string s2 inserted at index pos. 
# Returns empty string if pos is negative or pos > length of s. 

def insert(s1, s2, pos): 
    """ 
    >>> insert('', 'world!', 0)
    'world!'
    >>> insert('world!', 'I love the ', 0) 
    'I love the world!'
    >>> insert(' ', ' ', 0) 
    '  '
    >>> insert('', '', 0) 
    ''
    >>> insert('planet', 'refreshing our ', 0) 
    'refreshing our planet'
    >>> insert('Us!', 'Contact ', 0) 
    'Contact Us!'
    >>> insert('fdsafasd', 'w432fjdskajfdskbm,ade!', 5) 
    'fdsafw432fjdskajfdskbm,ade!asd'
    >>> insert("Trader Joe'", 's', 11) 
    "Trader Joe's"
    >>> insert('Trees and  rejoin the earth', 'plants', 10) 
    'Trees and plants rejoin the earth'
    >>> insert('None', 'None!', 4) 
    'NoneNone!'
    """ 

    i = 0
    ns = ''
    lst1 = []
    lst2 = []
    lst3 = []
    if s1 == '':
        return s2
    elif pos < 0 or pos > len(s1):
        return ''
    while i < pos:
        lst1 += s1[i]
        i += 1
    while pos < len(s1):
        lst2 += s1[pos]
        pos += 1
    for char in s2:
        lst3 += char

    newlist = lst1 + lst3 + lst2
    for x in newlist:
        ns += x
    return ns

# Returns a new string that is equivalent to string s with the character at pos replaced 
# with character c. Returns empty string if pos is negative or pos > length of s. 

def replace(s, pos, c):
    """
    >>> replace('hellos',5,'o')
    'helloo'
    >>> replace('plar',3,'y')
    'play'
    >>> replace('clover_money',7,'h')
    'clover_honey'
    >>> replace('tick',0,'k')
    'kick'
    >>> replace('',0,'ai')
    'ai'
    >>> replace('',0,'')
    ''
    >>> replace('    ',3,' ')
    '    '
    >>> replace('srbijadotokija',8,'milv')
    'srbijadomilvokija'
    >>> replace('uvek',0,'za')
    'zavek'
    >>> replace('jebacsamovaki',9,'t')
    'jebacsamotaki'
    """
    i = 0
    ns = ''
    lst=[]
    if pos == len(s):
        return s + c
    elif pos < 0 or pos > len(s):
        return ''
    for char in s:
        lst += char
    lst[pos] = c
    for elem in lst:
        ns += elem
    return ns

# Returns a new string consisting of the characters of string s from pos1 to pos2-1 inclusive. 
# Returns the empty string if there is no valid slice beginning at pos1 and ending at pos2-1.

def substring(s, pos1, pos2):
    """
    >>> substring('cat',0,3)
    'cat'
    >>> substring('potatoes',4,8)
    'toes'
    >>> substring('zvezdamijesve',0,6)
    'zvezda'
    >>> substring('najvisevolimkatarinu',12,20)
    'katarinu'
    >>> substring('fahfashkjhfasjhfashkl',3,6)
    'fas'
    >>> substring('',0,5)
    ''
    >>> substring('             ',0,2)
    '  '
    >>> substring('42342',0,9)
    ''
    >>> substring('diskoteka',-1,-1)
    ''
    >>> substring('ayujokreadsadsassssssssssssssssssssssssssssssa',0,20)
    'ayujokreadsadsasssss'
    """
    ns = ''
    lst = []
    if pos2 > len(s) or pos1 > pos2:
        return ""
    for char in s:
        lst += char
    for pos, elem in enumerate(lst):
        for numb in range(pos1, pos2):
            if pos == numb:
                ns += elem
    return ns

# Returns a new string that is equivalent to string s * n, where * is the string repetition 
# operator.

def repeatStr(s, n): 
    """ 
    >>> repeatStr('hello', 0) 
    ''
    >>> repeatStr('matador', 1) 
    'matador'
    >>> repeatStr('reduce', 2) 
    'reducereduce'
    >>> repeatStr('pollution', 3) 
    'pollutionpollutionpollution'
    >>> repeatStr('KanyeWest', 4) 
    'KanyeWestKanyeWestKanyeWestKanyeWest'
    >>> repeatStr('mirrors', 5) 
    'mirrorsmirrorsmirrorsmirrorsmirrors'
    >>> repeatStr('radio', 6) 
    'radioradioradioradioradioradio'
    >>> repeatStr('koka', 7) 
    'kokakokakokakokakokakokakoka'
    >>> repeatStr('prtibeegee', 8) 
    'prtibeegeeprtibeegeeprtibeegeeprtibeegeeprtibeegeeprtibeegeeprtibeegeeprtibeegee'
    >>> repeatStr('', 9) 
    ''
    """    
    ns=''
    if n == 0:
        s = ns
    while n > 0:
        ns += s
        n -= 1
    return ns

# Returns an integer that is the integer equivalent of the string s. 
# Assumes that s is the string version of a valid integer. Ex: str2int("106 ") -> 106 

def str2int(s):
    """
    >>> str2int('-1000092')
    -1000092
    >>> str2int('31232')
    31232
    >>> str2int('0')
    0
    >>> str2int('2121')
    2121
    >>> str2int('111111111')
    111111111
    >>> str2int('22')
    22
    >>> str2int('999999992')
    999999992
    >>> str2int('1389')
    1389
    >>> str2int('101010')
    101010
    >>> str2int('-22311')
    -22311
    """
    i = 0
    x = 0
    y = 0
    z = 1
    l1 = len(s) - 1
    l2 = len(s) - 1
    if s[0] == '-':
        while l1 > 0:
            y += (ord(s[z]) - 48) * 10**(l1 - 1)
            l1 -= 1
            z += 1
        return y * -1
    else:
        while l2 >= 0:
            i += (ord(s[x]) - 48) * 10**l2
            l2 -= 1
            x += 1
    return i

# Returns a string that is the string equivalent of valid integer i. Ex: int2str(-12) -> "-12 " 

def digits_list(n):
    ns=''
    lst1 = []
    lst2 = []
    if n == 0:
        lst2 += [n]
    elif n < 0:
        ns = chr(45)
        n= n * (-1)
    while n:
        last_digit = n % 10
        lst1 += [last_digit]
        n = n / 10
    for pos in range(len(lst1)-1, -1, -1):
        lst2 += [lst1[pos]]
    return lst2, ns

def int2str(i):
    """ 
    >>> int2str(-1000092) 
    '-1000092'
    >>> int2str(-1) 
    '-1'
    >>> int2str(0) 
    '0'
    >>> int2str(1) 
    '1'
    >>> int2str(10101000) 
    '10101000'
    >>> int2str(1389) 
    '1389'
    >>> int2str(100) 
    '100'
    >>> int2str(777) 
    '777'
    >>> int2str(69) 
    '69'
    >>> int2str(-2345) 
    '-2345'
    """
    ns = ''
    lst1 = []
    lst2, s = digits_list(i) 
    for elem in lst2:
        elem += 48
        lst1 += [chr(elem)]
    for elem in lst1:
        ns += elem
    return s + ns

#Returns a new list whose elements are each of the characters in string s as ordered in s

def string2list(s):
    """
    >>> string2list ('hello')
    ['h', 'e', 'l', 'l', 'o']
    >>> string2list ('3342222')
    ['3', '3', '4', '2', '2', '2', '2']
    >>> string2list ('')
    []
    >>> string2list ('svakipreda')
    ['s', 'v', 'a', 'k', 'i', 'p', 'r', 'e', 'd', 'a']
    >>> string2list ('finals')
    ['f', 'i', 'n', 'a', 'l', 's']
    >>> string2list ('playstation')
    ['p', 'l', 'a', 'y', 's', 't', 'a', 't', 'i', 'o', 'n']
    >>> string2list ('november-december')
    ['n', 'o', 'v', 'e', 'm', 'b', 'e', 'r', '-', 'd', 'e', 'c', 'e', 'm', 'b', 'e', 'r']
    >>> string2list ('shirt')
    ['s', 'h', 'i', 'r', 't']
    >>> string2list ('emergencyprocedures')
    ['e', 'm', 'e', 'r', 'g', 'e', 'n', 'c', 'y', 'p', 'r', 'o', 'c', 'e', 'd', 'u', 'r', 'e', 's']
    >>> string2list ('sibolou')
    ['s', 'i', 'b', 'o', 'l', 'o', 'u']
    """
    lst = []
    for char in s:
        lst += [char]
    return lst

#Returns a new string whose characters are each of elements of lst as ordered in lst
# You may assume lst is a list of strings

def list2string(lst):
    """
    >>> list2string (['h', 'e', 'l', 'l', 'o'])
    'hello'
    >>> list2string (['3', '3', '4', '2', '2', '2', '2'])
    '3342222'
    >>> list2string (['f'])
    'f'
    >>> list2string (['s', 'v', 'a', 'k', 'i', 'p', 'r', 'e', 'd', 'a'])
    'svakipreda'
    >>> list2string (['f', 'i', 'n', 'a', 'l', 's'])
    'finals'
    >>> list2string (['p', 'l', 'a', 'y', 's', 't', 'a', 't', 'i', 'o', 'n'])
    'playstation'
    >>> list2string ( ['n', 'o', 'v', 'e', 'm', 'b', 'e', 'r', '-', 'd', 'e', 'c', 'e', 'm', 'b', 'e', 'r'])
    'november-december'
    >>> list2string (['s', 'h', 'i', 'r', 't'])
    'shirt'
    >>> list2string (['e', 'm', 'e', 'r', 'g', 'e', 'n', 'c', 'y', 'p', 'r', 'o', 'c', 'e', 'd', 'u', 'r', 'e', 's'])
    'emergencyprocedures'
    >>> list2string (['s', 'i', 'b', 'o', 'l', 'o', 'u'])
    'sibolou'
    """
    ns=''
    for elem in lst:
        ns += elem
    return ns

# Returns a new string that contains all the characters of string s sorted in ascending order. 
# String s is converted to a list, sorted using selection sort, then converted back to a 
# string and returned. 
#Assumes s is a printable string, ie: characters have ASCII values between 32 and 255 
# inclusive.

def sortStr(s): 
    """ 
    >>> sortStr('helloeoruuivdworlkd sidoaepkmkjfla') 
    ' aadddeeefhiijkkkllllmooooprrsuuvw'
    >>> sortStr('') 
    ''
    >>> sortStr('                 sdsadasaaaaaaaaaa') 
    '                 aaaaaaaaaaaaddsss'
    >>> sortStr('fedcba') 
    'abcdef'
    >>> sortStr('987654321') 
    '123456789'
    >>> sortStr('naJED') 
    'DEJan'
    >>> sortStr('sdaaaaaaaaaaaaaaaaalk;dsaml;dsal;klk;ads23131-323fasmop') 
    '-11223333;;;;aaaaaaaaaaaaaaaaaaaaaddddfkkkllllmmopsssss'
    >>> sortStr('ji;sdaj;l;lkjkljkljkljk;k') 
    ';;;;adijjjjjjkkkkkkllllls'
    >>> sortStr('a                              ') 
    '                              a'
    >>> sortStr('finaltry') 
    'afilnrty'
    
    """
    s = string2list(s)
    for char1 in range(len(s)):
        min_index= char1
        span = 256
        for char2 in range(char1, len(s)):
            if ord(s[char2]) < span:
                span = ord(s[char2])
                index = char2
            char2 += 1
        s[index], s[min_index] = s[min_index], s[index]
    return list2string(s)

# Returns a new string containing all the characters of s sorted in ascending order, 
# employing a bucket sort with one bucket for each character O(n). 
# Assumes s is a printable string, ie: characters have ASCII values between 32 and 255 inclusive. 

def sortStr2(s):
    """ 
    >>> sortStr2('helloeoruuivdworlkd sidoaepkmkjfla') 
    ' aadddeeefhiijkkkllllmooooprrsuuvw'
    >>> sortStr2('') 
    ''
    >>> sortStr2('                 sdsadasaaaaaaaaaa') 
    '                 aaaaaaaaaaaaddsss'
    >>> sortStr2('fedcba') 
    'abcdef'
    >>> sortStr2('987654321') 
    '123456789'
    >>> sortStr2('naJED') 
    'DEJan'
    >>> sortStr2('sdaaaaaaaaaaaaaaaaalk;dsaml;dsal;klk;ads23131-323fasmop') 
    '-11223333;;;;aaaaaaaaaaaaaaaaaaaaaddddfkkkllllmmopsssss'
    >>> sortStr2('ji;sdaj;l;lkjkljkljkljk;k') 
    ';;;;adijjjjjjkkkkkkllllls'
    >>> sortStr2('a                              ') 
    '                              a'
    >>> sortStr2('finaltry') 
    'afilnrty'
    """
    ns = ''
    span = [0] * 256
    for char in s:
        num_value = ord(char)
        span[num_value] += 1             
    for elem in range(256):  
        if span[elem]:
            char = repeatStr(chr(elem), span[elem])
            ns += char
    return ns

if __name__ == '__main__':
    import doctest
    doctest.testmod()




