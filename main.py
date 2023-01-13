

def is_one_away(word1, word2):

    count = 0
    for c in word1:
        if c in word2:
            count += 1
    if len(word1) == len(word2) and count == len(word1) - 1:
        return True
    else:
        return False
w = input()
w1 =  input()
print(is_one_away(w,w1))