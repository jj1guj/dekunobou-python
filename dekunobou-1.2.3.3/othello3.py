import copy
import random
import sagasu2

def nyuryoku(teban,row,soutesu,sente,basyo):
    sagasu2.basyo_hyouji(basyo)
    for i, name in enumerate(basyo,1):
        print('{:02}_{}'.format(i,basyo[i-1]))
    basyo_utu=list(map(int,input("どこに打つか番号を入力してください：").split()))
    if (len(basyo_utu)==1 and basyo_utu[0]>len(basyo)) or len(basyo_utu)>1:
        basyo_utu=[]

    while len(basyo_utu)==0:
        basyo_utu=list(map(int,input("もう一度どこに打つか番号を入力してください：").split()))
        if len(basyo_utu)==1 and basyo_utu[0]>len(basyo):
            print("そこには打てません")
            basyo_utu=[]
        elif len(basyo_utu)>1:
            basyo_utu=[]

    if teban==sente:
        a=1
    else:
        a=2
    
    basyo_utu=basyo_utu[0]-1
    gyou=basyo[basyo_utu][0]-1
    retu=basyo[basyo_utu][1]-1
    row[gyou][retu]=a
    kaesi(row,gyou,retu,soutesu,sente)
    
def nyuryoku_auto(teban,row,soutesu,sente,basyo):
    gyou=basyo[0][0]
    retu=basyo[0][1]
    if teban==sente:
        a=1
    else:
        a=2
    row[gyou-1][retu-1]=a
    kaesi(row,gyou-1,retu-1,soutesu,sente)

def nyuryoku_random(teban,row,soutesu,sente,basyo):
    b=random.randrange(len(basyo))
    gyou=basyo[b][0]
    retu=basyo[b][1]
    if teban==sente:
        a=1
    else:
        a=2
    row[gyou][retu]=a
    kaesi(row,gyou-1,retu-1,sente,basyo)

def hyouji_teban(row,basyo):
    hyouji_r=copy.deepcopy(row)
    if len(basyo)>0:
        for i in range(len(basyo)):
            gyou_hyouji=basyo[i][0]
            retu_hyouji=basyo[i][1]
            hyouji_r[gyou_hyouji][retu_hyouji]='{:02}'.format(i+1)
    for i in range(8):
        for j in range(8):
            if hyouji_r[i][j]==0:
                hyouji_r[i][j]="＊"
            elif hyouji_r[i][j]==1:
                hyouji_r[i][j]="●"
            elif hyouji_r[i][j]==2:
                hyouji_r[i][j]="○"

            if j<7:
                print(str(hyouji_r[i][j]),end="")
            else:
                print(str(hyouji_r[i][j]))
                
def hyouji(row):
    hyouji_r=copy.deepcopy(row)
    for i in range(8):
        for j in range(8):
            if hyouji_r[i][j]==0:
                hyouji_r[i][j]="＊"
            elif hyouji_r[i][j]==1:
                hyouji_r[i][j]="●"
            elif hyouji_r[i][j]==2:
                hyouji_r[i][j]="○"

            if j<7:
                print(str(hyouji_r[i][j]),end="")
            else:
                print(str(hyouji_r[i][j]))

def kaesi(row,gyou,retu,soutesu,sente):
    if soutesu%2==sente:
        a=1
    else:
        a=2
    row[gyou][retu]=a
    i_gyou_migi=10
    i_gyou_hidari=10
    i_retu_ue=10
    i_retu_sita=10
    i_miginaname_ue=10
    i_miginaname_sita=10
    i_hidarinaname_ue=10
    i_hidarinaname_sita=10
    for i in range(1,8):
        #行方向
        #右から
        if i<8-retu and i<i_gyou_migi:
            if row[gyou][retu+i]==a:
                for j in range(i):
                    row[gyou][retu+j]=a
                i_gyou_migi=i
            elif row[gyou][retu+i]==0:
               i_gyou_migi=i
                
        #左から
        if i<retu+1 and i<i_gyou_hidari:
            if row[gyou][retu-i]==a:
                for j in range(i):
                    row[gyou][retu-j]=a
                i_gyou_hidari=i
            elif row[gyou][retu-i]==0:
                i_gyou_hidari=i

        #列方向
        #上から
        if i<8-gyou and i<i_retu_ue:
            if row[gyou+i][retu]==a:
                for j in range(i):
                    row[gyou+j][retu]=a
                i_retu_ue=i
            elif row[gyou+i][retu]==0:
                i_retu_ue=i
        #下から
        if i<gyou+1 and i<i_retu_sita:
            if row[gyou-i][retu]==a:
                for j in range(i):
                    row[gyou-j][retu]=a
                i_retu_sita=i
            elif row[gyou-i][retu]==0:
               i_retu_sita=i 

        #右斜め方向
        #上から
        if i<min(8-gyou,8-retu) and i<i_miginaname_ue:
            if row[gyou+i][retu+i]==a:
                for j in range(i):
                    row[gyou+j][retu+j]=a
                i_miginaname_ue=i
            elif row[gyou+i][retu+i]==0:
                i_miginaname_ue=i

        #下から
        if i<min(gyou+1,retu+1) and i<i_miginaname_sita:
            if row[gyou-i][retu-i]==a:
                for j in range(i):
                    row[gyou-j][retu-j]=a
                i_miginaname_sita=i
            elif row[gyou-i][retu-i]==0:
                i_miginaname_sita=i

        #左斜め方向
        #上から
        if i<min(8-gyou,retu+1) and i<i_hidarinaname_ue:
            if row[gyou+i][retu-i]==a:
                for j in range(i):
                    row[gyou+j][retu-j]=a
                i_hidarinaname_ue=i
            elif row[gyou+i][retu-i]==0:
                i_hidarinaname_ue=i

        #下から
        if i<min(gyou+1,8-retu) and i<i_hidarinaname_sita:
            if row[gyou-i][retu+i]==a:
                for j in range(i):
                    row[gyou-j][retu+j]=a
                i_hidarinaname_sita=i
            elif row[gyou-i][retu+i]==0:
                i_hidarinaname_sita=i
    return row

def kazu(row):
    ichi=0
    ni=0
    kazu=[]
    for i in range(8):
        ichi=ichi+row[i].count(1)
        ni=ni+row[i].count(2)
    kazu=[ichi,ni]
    return kazu
    #return ichi,ni

def hantei(row,basyo,soutesu,sente):
    a=0
    if soutesu==1:
        a=random.randint(0,len(basyo)-1)
        if soutesu%2==sente:
            row[basyo[a][0]][basyo[a][1]]=1
        else:
            row[basyo[a][0]][basyo[a][1]]=2
    elif len(basyo)==1:
        a=0
        if soutesu%2==sente:
            row[basyo[a][0]][basyo[a][1]]=1
        else:
            row[basyo[a][0]][basyo[a][1]]=2
    else:
        a=random.randint(0,len(basyo)-1)
        if soutesu%2==sente:
            row[basyo[a][0]][basyo[a][1]]=1
        else:
            row[basyo[a][0]][basyo[a][1]]=2
    return basyo[a]
