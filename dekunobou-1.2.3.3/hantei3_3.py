import time
import copy
import random
import othello3
import sagasu2_hantei2

#()内s,t: 場所数、枚数の得点配分
def hantei(row,basyo1,kazu,simulate,a,soutesu,sente,s,t):
    if soutesu%2==sente:
        a=0
        b=1
    else:
        a=1
        b=0

    basyo_count=[]
    simulate=[]
    hantei1=[]  #[打てる場所数の差分,枚数の差分]
    basyosu=0
    maisu=0

    utu=[]
    
    tokuten=[]
    for i in range(len(basyo1)):
        okenai=0
        simulate.append(copy.deepcopy(row))
        simulate[i]=othello3.kaesi(simulate[i],basyo1[i][0],basyo1[i][1],soutesu,sente)
        basyo2=[]
        kazu_count=[]
        basyo2,okenai=sagasu2_hantei2.sagasu(simulate[i],soutesu+1,sente,basyo2,okenai)
        basyo_count.append(basyo2)
        kazu_count=othello3.kazu(simulate[i])
        basyosu=len(basyo1)-len(basyo_count[i])
        maisu=kazu_count[a]-kazu_count[b]
        tokuten=s*basyosu-t*okenai
        if [0,0] in basyo2 or [0,7] in basyo2 or [7,0] in basyo2 or [7,7] in basyo2:
            tokuten=tokuten-1
        elif  [0,1] in basyo2 or [0,6] in basyo2 or [1,0] in basyo2 or [1,1] in basyo2 or [1,6] in basyo2 or\
              [1,7] in basyo2 or [6,0] in basyo2 or [6,1] in basyo2 or [6,6] in basyo2 or [6,7] in basyo2 or\
              [7,1] in basyo2 or [7,6] in basyo2:
            tokuten=tokuten+1
        hantei1.append(tokuten)

    """
    print("評価値")
    if soutesu%2==sente:
        print("先手"+str(max(hantei1))+" vs "+str(-1*max(hantei1))+"後手")
    else:
        print("先手"+str(-1*max(hantei1))+" vs "+str(max(hantei1))+"後手")

    saidai_count=0
    for j in range(len(hantei1)):
        if hantei1[j]>=max(hantei1):
            saidai_count=saidai_count+1
    
    print(str(max(hantei1)),",",str(saidai_count))
    """
    utu=[k for k, x in enumerate(hantei1) if x==max(hantei1)]
    a=random.randint(0,len(utu)-1)
            
    a=utu[a]

    return a
