def reverse(text):
    ret=""
    for i in range(len(text)):
        ret=ret+text[-i-1]
    print text+'->'+ret
    return ret

if __name__ == '__main__':  
    reverse("ABCD")
