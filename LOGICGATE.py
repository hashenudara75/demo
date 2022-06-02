print("\n\tI can work with SOP , Truth table & Karnaugh map")
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','=','(',')',',',"'",'+',                    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','=','(',')',',',"'",'+',                    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list3=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print("hashe")

while True:
    allchar=[]
    print("\n\t\t1.Truth table > SOP,POS & Karnaugh MAP")
    print("\n\t\t2.SOP > Standed SOP, POS, Karnaugh MAP and Truth table")
    option=input("\n\t\tSelect a option(1/2) : ")
    
    
    
    print("\n\t---------------------------------------------------")
    
    
    if option=="1":
        allcharnum=int(input("\n\tNumber variables of variables : "))
        header="\n\n\n\n\t"
        
        stri=""
        for k in range(0,allcharnum+1):
            stri+="--------"
        
        #creating allchar list & header
        
        
        for k in range(0,allcharnum):
            allchar.append(list3[k])
            header+=list3[k]+"\t"
        print(header+"Output")
        
        print("      "+stri)

        #print(allchar)
        blogic1=[] ; blogic2=[] ; blogic4=[]
        
        #body
        rows=2**allcharnum
        for k in range(0,rows):
            num=k ; tempnn="" ; tempnn1="" 
            binary=""
            output_binary=""
            x=1

            while 0!=num:
                binary=binary+str(num%2)
                num=num//2


            while x<=len(binary):
                output_binary=output_binary+binary[len(binary)-x]
                x+=1

            
            while len(output_binary)!=allcharnum:
                output_binary="0"+output_binary
            #print(output_binary)
            
            rowout="\t"
            for qq in output_binary:
                rowout+=qq+"\t"
            f=input(rowout)
            print("      "+stri)
            y11=0 ; y12=0
            if f=="1":
                y11=(output_binary)
            else:
                y12=(output_binary)
        
            #print(y11)
            if y11!=0 :
                jo=0
                for i in y11:
                
                    if i =="1":
                        cv=allchar[jo]+" "
                        
                    if i=="0":
                        cv=allchar[jo]+"'"
                    tempnn+=(cv)
                    jo+=1
                blogic2.append(tempnn)
            if y12!=0:
                jo=0
                for i in y12:
                    if i =="0":
                        cv=allchar[jo]+'+'
                    if i=="1":
                        cv=allchar[jo]+"'"+'+'
                    tempnn1+=cv
                    jo+=1
                
                blogic4.append('('+tempnn1[0:len(tempnn1)-1]+')')
                
                


        #print(allchar)
        #print("blogic2",blogic2)
        #print("blogic3",blogic3)
        #print("blogic4",blogic4)

        finalsop=blogic2




    #print("---------------------------------------------------------------")
    #========================================================================================================================================================================================================================================================================================
    if option=="2":
        print("\n\tUse this format to input your SOP - Dont use spaces")
        print("\n\t\tf=(variable1,variable2,...)=variable+...")
        print("\n\t\t\tex: f(A,B,C,D)=AB+D'")
        print("\n\t\t\t\t -OR-")
        print("\n\t\tvariable1+variable2+...")
        print("\n\t\t\tex: AB'+D'+CDA")
        print("\n\t---------------------------------------------------")
       
        num=n=input("\n\tEnter SOP :  ")

        allchar=[];inp=[] ; a1=[]

        #simple to capital
        txt=n ; qqqq="capital"
        x=0 
        output=""
        

        while x!=len(txt):
            k=0
            while not(list1[k]==txt[x]):
                k+=1
            output=output+list2[k]
            x+=1
        num=n=output
        #print(output)
        #print(n,num)
        #f(a,b,c,d)=
        oi=0 ; xx=0
        if n[0]+n[1]=="F(":
            for k in range(0,len(n)):
                if oi==0:
                    
                    if n[k]==")":
                        xx=k-1
                        oi=1
        if xx!=0:
            for jj in range(2,xx+1):
                if n[jj]!=",":
                    allchar.append(n[jj])
            tempn=""
            for fff in range(xx+3,len(n)):
                tempn+=n[fff]
                
            n=tempn
            num=tempn
            


        if xx==0:
            allchar.append(n[0])
            #GET ALL CHAR
            k=1
            while k<len(n):
                if not(n[k] in allchar) and n[k]!="'" and n[k]!="+":
                    allchar.append(n[k])
                k=k+1



        #print("allchar",len(allchar))
        allchartemp=[]
        #reorganize allchar in ALPABATICAL ODER (A-Z)
        for k in list3:
            if k in allchar:
                allchartemp.append(k)

        allchar=allchartemp

        #print(allchar)


        #SPLITING
        inp=num.split("+")


        #print("1inp",inp)

        #FIRST ADDING VALUE THAT HAVE ALL CHARS WHEN INPUT
        
        for k in inp:
            count=0
            for j in allchar:
                if j in k:
                    count+=1
            if count==len(allchar): a1.append(k)
        if len(allchar)>5 and len(a1)!=len(inp): print("\n\tSubmited SOP have %d variables, \n\tSo this process get more few seconds and more CPU usage \n\tProcessing your output..."%len(allchar))
            

        #print(count)
        #print("a1",a1)
        #checking for all are standed sop values
        command="c2ssop"
        if len(a1)==len(inp): command="dc2ssop"
        
        #print(command)
        if command=="c2ssop":
            #ADDING ( C+C' )

            p=0
            while p<len(allchar):
                k=0
                while k<len(inp):
                    '''count=0
                    for j in inp[k]:
                        if j=="'":
                            count+=1
                    print(count)'''
                    for j in allchar:
                        if not(j in inp[k]):
                            a1.append(inp[k]+j+" ")
                            a1.append(inp[k]+j+"'")

                    k+=1
                inp=a1
                p+=1

        #print("a12",a1)
        #DLETEING VALUES THAT UNUSEFUL OR NOT HAVE ALL THE CHAR
        out1=[]
        #print(inp)
        for k in inp:
            check=0
            for i in allchar:
                if (i in k):
                    check+=1
            if check==len(allchar):
                out1.append(k)
        #print("out1",out1)



        #ORGANIZING LETTERS ACCODING TO ALPABATICAL (A-Z) ODER
        out2=[] #OUT2 HAVE A-Z ODER
        k=0 
        while k<len(out1):
            j=0
            sum=""
            while j<len(allchar):
                d=0
                while d<len(out1[k]):
                    if allchar[j]==out1[k][d]:
                        if d<len(out1[k])-1:
                            if out1[k][d+1]=="'":
                                sum+=allchar[j]+"'"
                            else:
                                sum+=allchar[j]+" "
                        else:
                            sum+=allchar[j]+" "
                    d+=1
                j+=1
            out2.append(sum)
            k+=1



        #DELETING SAME VALUES IN OUT2 (FINAL STEP OF SOP)
        finalsop=[]
        finalsop.append(out2[0])
        for k in out2:
            if not(k in finalsop):
                finalsop.append(k)
                
                
        #print("final",finalsop)
    if option=="1" or option=="2":
        #SOP SECTOIN : ALL ARE DONE > NOW OUTPUT THE FINAL
        final=""
        for k in range(0,len(finalsop)-1):
            final+=finalsop[k] + " + "

        final+=finalsop[-1]
        #print(len(finalsop))   
        print("\n\n\n\n\t\t\t --- Standed SOP:  ---")
        print("\n\n\n\t", final)



        #========================================================================================================================================================================================================================================================================================
        rowslist=[]

        if len(allchar)>6 : print("\n\n\n\nI can't draw the Karnaugh Map, must have 4 variables or lower")
        else:
            #creating kano header and 1st colum
            print("\n\n\n\n\t\t\t --- Karnaugh map ---")
            k=0 ; i=0
            if len(allchar)==2:
                header=[allchar[0]+"'",allchar[0]+" "]
                colum=[(allchar[1]+"'"),( allchar[1]+" ")]
                rows=2 ; colums=2 
            if len(allchar)==3:
                header=[(allchar[0]+"'"+allchar[1]+"'"),(allchar[0]+"'"+allchar[1]+" "),(allchar[0]+" "+allchar[1]+" "),(allchar[0]+" "+allchar[1]+"'")]
                colum=[(allchar[2]+"'"),( allchar[2]+" ")]
                colums=4 ; rows=2
            if len(allchar)==4:
                header=[(allchar[0]+"'"+allchar[1]+"'"),(allchar[0]+"'"+allchar[1]+" "),(allchar[0]+" "+allchar[1]+" "),(allchar[0]+" "+allchar[1]+"'")]
                colum=[(allchar[2]+"'"+allchar[3]+"'"),(allchar[2]+"'"+allchar[3]+" "),(allchar[2]+" "+allchar[3]+" "),(allchar[2]+" "+allchar[3]+"'")]
                colums=4 ; rows=4
            if len(allchar)==5:
                header=[(allchar[0]+"'"+allchar[1]+"'"+allchar[2]+"'"),(allchar[0]+"'"+allchar[1]+"'"+allchar[2]+" "),(allchar[0]+"'"+allchar[1]+" "+allchar[2]+" "),(allchar[0]+"'"+allchar[1]+" "+allchar[2]+"'"),(allchar[0]+" "+allchar[1]+"'"+allchar[2]+"'"),(allchar[0]+" "+allchar[1]+"'"+allchar[2]+" "),(allchar[0]+" "+allchar[1]+" "+allchar[2]+" "),(allchar[0]+" "+allchar[1]+" "+allchar[2]+"'")]
                colum=[(allchar[3]+"'"+allchar[4]+"'"),(allchar[3]+"'"+allchar[4]+" "),(allchar[3]+" "+allchar[4]+" "),(allchar[3]+" "+allchar[4]+"'")]
                colums=8 ; rows= 4
            if len(allchar)==6:
                header=[(allchar[0]+"'"+allchar[1]+"'"+allchar[2]+"'"),(allchar[0]+"'"+allchar[1]+"'"+allchar[2]+" "),(allchar[0]+"'"+allchar[1]+" "+allchar[2]+" "),(allchar[0]+"'"+allchar[1]+" "+allchar[2]+"'"),(allchar[0]+" "+allchar[1]+"'"+allchar[2]+"'"),(allchar[0]+" "+allchar[1]+"'"+allchar[2]+" "),(allchar[0]+" "+allchar[1]+" "+allchar[2]+" "),(allchar[0]+" "+allchar[1]+" "+allchar[2]+"'")]
                colum=[(allchar[3]+"'"+allchar[4]+"'"+allchar[5]+"'"),(allchar[3]+"'"+allchar[4]+"'"+allchar[5]+" "),(allchar[3]+"'"+allchar[4]+" "+allchar[5]+" "),(allchar[3]+"'"+allchar[4]+" "+allchar[5]+"'"),(allchar[3]+" "+allchar[4]+"'"+allchar[5]+"'"),(allchar[3]+" "+allchar[4]+"'"+allchar[5]+" "),(allchar[3]+" "+allchar[4]+" "+allchar[5]+" "),(allchar[3]+" "+allchar[4]+" "+allchar[5]+"'")]
                colums=8 ; rows=8
            #print(len(header))
            #print(colum[0])
            
            #drawing kano
                
            for k in range(0,rows):
                i=0
                while i<colums:
                    if (header[i]+colum[k] in finalsop):
                        rowslist.append("1")
                    else: rowslist.append("0")            
                    i+=1    
            
            print("\n\n\n")
            if len(allchar)==3:
                print("\t"+"\t"+"\t"+header[0]+"\t"+header[1]+"\t"+header[2]+"\t"+header[3]+"\n")
                print("\t"+"\t"+colum[0]+"\t "+rowslist[0]+"\t "+rowslist[1]+"\t "+rowslist[2]+"\t "+rowslist[3]+"\n")
                print("\t"+"\t"+colum[1]+"\t "+rowslist[4]+"\t "+rowslist[5]+"\t "+rowslist[6]+"\t "+rowslist[7]+"\n")

            if len(allchar)==2:
                print("\t"+"\t"+"\t"+header[0]+"\t"+header[1]+"\n")
                print("\t"+"\t"+colum[0]+"\t"+rowslist[0]+"\t"+rowslist[1]+"\n")
                print("\t"+"\t"+colum[1]+"\t"+rowslist[2]+"\t"+rowslist[3]+"\n")
                
            if len(allchar)==4:
                print("\t"+"\t"+"\t"+header[0]+"\t"+header[1]+"\t"+header[2]+"\t"+header[3]+"\n")
                print("\t"+"\t"+colum[0]+"\t "+rowslist[0]+"\t "+rowslist[1]+"\t "+rowslist[2]+"\t "+rowslist[3]+"\n")
                print("\t"+"\t"+colum[1]+"\t "+rowslist[4]+"\t "+rowslist[5]+"\t "+rowslist[6]+"\t "+rowslist[7]+"\n")
                print("\t"+"\t"+colum[2]+"\t "+rowslist[8]+"\t "+rowslist[9]+"\t "+rowslist[10]+"\t "+rowslist[11]+"\n")
                print("\t"+"\t"+colum[3]+"\t "+rowslist[12]+"\t "+rowslist[13]+"\t "+rowslist[14]+"\t "+rowslist[15]+"\n")
            if len(allchar)==5:
                print("\t"+"\t"+"\t"+header[0]+"\t"+header[1]+"\t"+header[2]+"\t"+header[3]+"\t"+header[4]+"\t"+header[5]+"\t"+header[6]+"\t"+header[7]+"\n")
                print("\t"+"\t"+colum[0]+"\t "+rowslist[0]+"\t "+rowslist[1]+"\t "+rowslist[2]+"\t "+rowslist[3]+"\t "+rowslist[4]+"\t "+rowslist[5]+"\t "+rowslist[6]+"\t "+rowslist[7]+"\n")
                print("\t"+"\t"+colum[1]+"\t "+rowslist[8]+"\t "+rowslist[9]+"\t "+rowslist[10]+"\t "+rowslist[11]+"\t "+rowslist[12]+"\t "+rowslist[13]+"\t "+rowslist[14]+"\t "+rowslist[15]+"\n")
                print("\t"+"\t"+colum[2]+"\t "+rowslist[16]+"\t "+rowslist[17]+"\t "+rowslist[18]+"\t "+rowslist[19]+"\t "+rowslist[20]+"\t "+rowslist[21]+"\t "+rowslist[22]+"\t "+rowslist[23]+"\n")
                print("\t"+"\t"+colum[3]+"\t "+rowslist[24]+"\t "+rowslist[25]+"\t "+rowslist[26]+"\t "+rowslist[27]+"\t "+rowslist[28]+"\t "+rowslist[29]+"\t "+rowslist[30]+"\t "+rowslist[31]+"\n")
                
            if len(allchar)==6:
                print("\t"+"\t"+"\t"+header[0]+"\t"+header[1]+"\t"+header[2]+"\t"+header[3]+"\t"+header[4]+"\t"+header[5]+"\t"+header[6]+"\t"+header[7]+"\n")
                print("\t"+"\t"+colum[0]+"\t "+rowslist[0]+"\t "+rowslist[1]+"\t "+rowslist[2]+"\t "+rowslist[3]+"\t "+rowslist[4]+"\t "+rowslist[5]+"\t "+rowslist[6]+"\t "+rowslist[7]+"\n")
                print("\t"+"\t"+colum[1]+"\t "+rowslist[8]+"\t "+rowslist[9]+"\t "+rowslist[10]+"\t "+rowslist[11]+"\t "+rowslist[12]+"\t "+rowslist[13]+"\t "+rowslist[14]+"\t "+rowslist[15]+"\n")
                print("\t"+"\t"+colum[2]+"\t "+rowslist[16]+"\t "+rowslist[17]+"\t "+rowslist[18]+"\t "+rowslist[19]+"\t "+rowslist[20]+"\t "+rowslist[21]+"\t "+rowslist[22]+"\t "+rowslist[23]+"\n")
                print("\t"+"\t"+colum[3]+"\t "+rowslist[24]+"\t "+rowslist[25]+"\t "+rowslist[26]+"\t "+rowslist[27]+"\t "+rowslist[28]+"\t "+rowslist[29]+"\t "+rowslist[30]+"\t "+rowslist[31]+"\n")
                print("\t"+"\t"+colum[4]+"\t "+rowslist[32]+"\t "+rowslist[33]+"\t "+rowslist[34]+"\t "+rowslist[35]+"\t "+rowslist[36]+"\t "+rowslist[37]+"\t "+rowslist[38]+"\t "+rowslist[39]+"\n")
                print("\t"+"\t"+colum[5]+"\t "+rowslist[40]+"\t "+rowslist[41]+"\t "+rowslist[42]+"\t "+rowslist[43]+"\t "+rowslist[44]+"\t "+rowslist[45]+"\t "+rowslist[46]+"\t "+rowslist[47]+"\n")
                print("\t"+"\t"+colum[6]+"\t "+rowslist[48]+"\t "+rowslist[49]+"\t "+rowslist[50]+"\t "+rowslist[51]+"\t "+rowslist[52]+"\t "+rowslist[53]+"\t "+rowslist[54]+"\t "+rowslist[55]+"\n")
                print("\t"+"\t"+colum[7]+"\t "+rowslist[56]+"\t "+rowslist[57]+"\t "+rowslist[58]+"\t "+rowslist[59]+"\t "+rowslist[60]+"\t "+rowslist[61]+"\t "+rowslist[62]+"\t "+rowslist[63]+"\n")
                
                

        
        
        
        #========================================================================================================================================================================================================================================================================================
        #print("\n\t---------------------------------------------------")
        
        if option=="2":
            blogic4=[]
            print("\n\t---------------------------------------------------")

            #truth table
            print("\n\n\n\n\t\t\t --- Truth Table ---")
            output_binary=""
            binary=""
            #header
            header="\n\n\n\n\t\t"
            for k in allchar:
                header+=k+"\t"
            print(header+"Output")
            
            
            #body logic
            blogic=[] ; 
            for k in finalsop:
                tempn=""
                for i in range(0,len(k),+1):
                    if k[i]==" ": tempn+=("1")
                    elif k[i]=="'": tempn+=("0")
                blogic.append(tempn)
            #print(blogic)
            stri=""
            for k in range(0,len(allchar)+1):
                stri+="--------"
            print("\t"+"      "+stri)
            #body
            rows=2**len(allchar)
            for k in range(0,rows):
                num=k
                binary=""
                output_binary=""
                x=1

                while 0!=num:
                    binary=binary+str(num%2)
                    num=num//2


                while x<=len(binary):
                    output_binary=output_binary+binary[len(binary)-x]
                    x+=1

                
                while len(output_binary)!=len(allchar):
                    output_binary="0"+output_binary
                #print(output_binary)
                if (output_binary in blogic):
                    f="1"
                    
                else: 
                    f="0" ; jj=0 ;cv=""
                    for tt in output_binary:
                        if tt=="0":
                            cv+=allchar[jj]+"+"
                            #blogic4.append(allchar[jj]+"+")
                        else:
                            cv+=allchar[jj]+"'"+"+"
                        jj+=1
                    blogic4.append('('+cv[0:len(cv)-1]+")")
                        
                rowout="\t"
                for qq in output_binary:
                    rowout+=qq+"\t"
                print("\t"+rowout+f)
                print("\t"+"      "+stri)
            
    
        if option=="1" or option=="2":
            print("\n\n\n\n\t\t\t ------   POS  ------")
            #print("\n\n\n\n\t\t\t --- Standed SOP  ---")
            pos=""
            for ppp in blogic4:
                pos+=ppp
                
            print("\n\n\n\t", pos)
            
        print("\n\n\n\n\t---------------------------------------------------")
    
    
    else : print("\n\tinvalid option, chose 1 or 2 ")
    
    
    
    
    
    
    
    
    
    
    
    
