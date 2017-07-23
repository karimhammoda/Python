'''
Created on Jul 7, 2017

@author: Karim Hammouda
'''

def anagram_solution3(s1,s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok

def anagram_solutionkiki(word1,word2):

    if len(word1) != len(word2):
        return False
    else:
        histogram1 = dict()
        histogram2 = dict()
        for character in word1:
            histogram1[character] =  histogram1.get(character , 0) + 1
        print(histogram1)
        
        for character in word2:
            histogram2[character] =  histogram2.get(character , 0) + 1
        print(histogram2)
        
        for key in histogram1.keys():
            if histogram1[key] != histogram2.get(key, 0):
                return False
        return True

def anagram_solution2(s1,s2):
    a_list1 = list(s1)
    a_list2 = list(s2)
    a_list1.sort()
    a_list2.sort()
    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if a_list1[pos] == a_list2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches
    

def main():

    print(anagram_solutionkiki('Kaaaareeem','eaaaaKreem'))
    return


if __name__ == '__main__':
    main()