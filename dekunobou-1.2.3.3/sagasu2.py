def sagasu(row,soutesu,sente,basyo):
    if soutesu%2==sente:
        a=2
        b=1
    else:
        a=1
        b=2
        
    for i in range(8):
        for j in range(8):
            #行方向
            if j<=6:
                if row[i][j]==0 and row[i][j+1]==a:
                    row_migi(row,i,j,b,basyo)
                elif row[i][j]==a and row[i][j+1]==0:
                    row_hidari(row,i,j+1,b,basyo)
            #列方向
            if i<=6:
                if row[i][j]==0 and row[i+1][j]==a:
                    clm_ue(row,i,j,b,basyo)
                elif row[i][j]==a and row[i+1][j]==0:
                    clm_sita(row,i+1,j,b,basyo)
            #斜め方向
            for k in range(6):
                
                if j<=6-k:
                    #盤面下部
                    #右斜め方向
                    if row[j+k][j]==0 and row[j+k+1][j+1]==a:
                        miginaname_ue(row,j+k,j,b,basyo)
                    elif row[j+k][j]==a and row[j+k+1][j+1]==0:
                        miginaname_sita(row,j+k+1,j+1,b,basyo)

                    #左斜め方向
                    if row[j+k][7-j]==0 and row[j+k+1][7-(j+1)]==a:
                        hidarinaname_ue(row,j+k,7-j,b,basyo)
                    elif row[j+k][7-j]==a and row[j+k+1][7-(j+1)]==0:
                        hidarinaname_sita(row,j+k+1,7-(j+1),b,basyo)
                        
                    #盤面上部
                    if k>0:
                        #右斜め方向
                        if row[j][j+k]==0 and row[j+1][j+k+1]==a:
                            miginaname_ue(row,j,j+k,b,basyo)
                        elif row[j][j+k]==a and row[j+1][j+k+1]==0:
                            miginaname_sita(row,j+1,j+k+1,b,basyo)

                        #左斜め方向
                        if row[j][7-(j+k)]==0 and row[j+1][7-(j+k+1)]==a:
                            hidarinaname_ue(row,j,7-(j+k),b,basyo)
                        elif row[j][7-(j+k)]==a and row[j+1][7-(j+k+1)]==0:
                            hidarinaname_sita(row,j+1,7-(j+k+1),b,basyo)
                    

    return basyo

def row_migi(row,x,y,b,basyo):
    for i in range(2,8-y):
        if row[x][y+i]==b and [x,y] not in basyo:
            basyo.append([x,y])
            break
        elif row[x][y+i]==0:
            break

def row_hidari(row,x,y,b,basyo):
    for i in range(2,y+1):
        if row[x][y-i]==b and [x,y] not in basyo:
            basyo.append([x,y])
            break
        elif row[x][y-i]==0:
            break
    
def clm_ue(row,x,y,b,basyo):
    for i in range(2,8-x):
        if row[x+i][y]==b and [x,y] not in basyo:
            basyo.append([x,y])
            break
        elif row[x+i][y]==0:
            break

def clm_sita(row,x,y,b,basyo):
    for i in range(2,x+1):
        if row[x-i][y]==b and [x,y] not in basyo:
            basyo.append([x,y])
            break
        elif row[x-i][y]==0:
            break

def miginaname_ue(row,x,y,b,basyo):
    for i in range(2,min(8-x,8-y)):
        if row[x+i][y+i]==b and [x,y] not in basyo:
            basyo.append([x,y])
            break
        elif row[x+i][y+i]==0:
            break
    
def miginaname_sita(row,x,y,b,basyo):
    for i in range(2,min(x+1,y+1)):
        if row[x-i][y-i]==b and [x,y] not in basyo:
            basyo.append([x,y])
            break
        elif row[x-i][y-i]==0:
            break
        
def hidarinaname_ue(row,x,y,b,basyo):
    for i in range(2,min(8-x,y+1)):
        if row[x+i][y-i]==b and [x,y] not in basyo:
            basyo.append([x,y])
            break
        elif row[x+i][y-i]==0:
            break
        
def hidarinaname_sita(row,x,y,b,basyo):
    for i in range(2,min(x+1,8-y)):
        if row[x-i][y+i]==b and [x,y] not in basyo:
            basyo.append([x,y])
            break
        elif row[x-i][y+i]==0:
            break
    

def basyo_hyouji(basyo):
    for i in range(len(basyo)):
        basyo[i][0]=basyo[i][0]+1
        basyo[i][1]=basyo[i][1]+1
    return basyo
