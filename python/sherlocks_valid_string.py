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
    
    counts = [char_count[k] for k in char_count]
    print(counts)
    # will check if 1 character has been removed from 1 index
    removed_one = False
    # the current count initialize to the first element in count
    current_count = counts[0]

    for n in counts:
        # if the character occurs the same number of times
        if n == current_count:
            continue
        # if you can remove on character from one index
        elif n - 1 == current_count or n + 1 == current_count or n == 1:
            # if one character has already been removed
            if removed_one:
                return "NO"

            # set removed to true
            removed_one = True
        else:
            return "NO"

    return "YES"
    

print(isValid('aaaabbcc')) #NO
print(isValid('aabbccddd')) #NO
print(isValid('ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'))