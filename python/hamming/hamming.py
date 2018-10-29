def distance(strand_a, strand_b):
    if len(strand_a)!=len(strand_b): raise Exception(ValueError)

    dist=0
    
    for i in range(0,len(strand_a)):
        if strand_a[i]!=strand_b[i]: dist=dist+1
    
    return dist
