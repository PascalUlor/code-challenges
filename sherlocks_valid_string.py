def isValid(s):
    # get the number of occurrence of each character
    # create a counter to log number of occurrnce of charaters
    # cache number of occurrence of each character in dict
    # if  all char occur is even or odd occur not > 1 return true
    # else false
    char_count = {}
    for i in range(0, len(s)):
        if s[i] in char_count:
            char_count[s[i]] = char_count[s[i]] + 1
        else:
            char_count[s[i]] = 1
    
    odd_count = 0
    counts = [char_count[k] for k in char_count]
    evens = [char_count[k] for k in char_count if char_count[k]%2 == 0]
    print(counts)
    for i in range(0, len(counts)):
        if counts[i]%2 != 0:
            odd_count += 1
    
    if len(set(evens)) > 1 or odd_count > 1:
        return 'NO'
    
    if odd_count > 1:
        return 'NO'
    else:
        return 'YES'
    

# print(isValid('aaaabbcc'))
# print(isValid('aabbcd'))
print(isValid('ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'))