import time
import copy
import random
import othello3
import sagasu2
import hantei3_3

sente=1
gote=0
soutesu=1

change_kaisu=0

row1=[0,0,0,0,0,0,0,0]
row2=[0,0,0,0,0,0,0,0]
row3=[0,0,0,0,0,0,0,0]
row4=[0,0,0,2,1,0,0,0]
row5=[0,0,0,1,2,0,0,0]
row6=[0,0,0,0,0,0,0,0]
row7=[0,0,0,0,0,0,0,0]
row8=[0,0,0,0,0,0,0,0]

row=[row1,row2,row3,row4,row5,row6,row7,row8]
basyo=[]
simulate=[]

a=0

print("あなたの手番を選択してください。")
teban=input("先手の場合はsを、後手の場合はgを選択してください：")
if teban=="s":
    teban1=teban
    teban=sente
    print("先手")
else:
    teban1=teban
    teban=gote
    print("後手")

#othello3.hyouji(row)
start=time.time()
while soutesu<60:
    basyo=[]
    simulate=[]
    
    kazu=othello3.kazu(row)
    soutesu=kazu[0]+kazu[1]-3
    print("総手数："+str(soutesu))
    
    if soutesu==1:
        print("初手")
    else:
        print(str(soutesu)+"手目")
    print("sente="+str(sente))
    print("先手:"+str(kazu[0])+"vs"+str(kazu[1])+"後手")
    if soutesu%2==teban:
        sagasu2.sagasu(row,soutesu,sente,basyo)
        othello3.hyouji_teban(row,basyo)
        if len(basyo)==0:
            change=input("置く場所がないので相手の手番に移ります[Y/n]")
            change_kaisu=change_kaisu+1
            if sente==1:
                sente=0
                gote=1
            else:
                sente=1
                gote=0
        else:
            change_kaisu=0
            othello3.nyuryoku(teban,row,soutesu,sente,basyo)
    else:
        start=time.time()
        sagasu2.sagasu(row,soutesu,sente,basyo)
        othello3.hyouji(row)
        if len(basyo)==0:
            change_kaisu=change_kaisu+1
            if sente==1:
                sente=0
                gote=1
            else:
                sente=1
                gote=0
        else:
            change_kaisu=0
            if teban==sente:
                a=hantei3_3.hantei(row,basyo,kazu,simulate,a,soutesu,sente,0.65,0.35)
            else:
                a=hantei3_3.hantei(row,basyo,kazu,simulate,a,soutesu,sente,0.54,0.46)
            
            print("["+str(basyo[a][0]+1)+", "+str(basyo[a][1]+1)+"]")
            row=othello3.kaesi(row,basyo[a][0],basyo[a][1],soutesu,sente)

    if teban1=="s":
        teban=sente
    else:
        teban=gote
    if change_kaisu>=2:
        break
    end=time.time()

print("")
othello3.hyouji(row)
kazu=othello3.kazu(row)
print("先手:"+str(kazu[0])+"vs"+str(kazu[1])+"後手")
if kazu[0]>kazu[1]:
    print("先手の勝ちです")
elif kazu[0]<kazu[1]:
    print("後手の勝ちです")
else:
    print("引き分けです")
