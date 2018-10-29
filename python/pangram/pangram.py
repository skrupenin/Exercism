def is_pangram(sentence):
    s=sentence.lower()
 
    for n in range(97, 123):    
        if s.find(n)==-1: return False

    return True
    
if __name__ == '__main__': print is_pangram('aaa')