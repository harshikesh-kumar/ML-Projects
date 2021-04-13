import tkinter
from tkinter import*
j,k,l=0,0,0
def evm1():
    global j
    j+=1 
    #print('voted to BJP=',j)
    #return(j)
def evm2():
    global k
    k+=1
    #print('voted to CONGRESS=',k)
    #return(k)
def evm3():
    global l
    l+=1
   # print('voted to AAP=',l)
    #return(l)
def total():
    print('total votes of BJP={}\n total votes of CONGRESS={}\n total votes of AAP={}'.format(j,k,l))
    if j==k or j==l or k==l:
        print('Tie')
            
    elif j>=k and j>=l:
        print('BJP won the election')
            
    elif k>=j and k>=l:
        print('CONGRESS won the election')
        
    else :
        print('AAP won the election')
a=Tk()
a.title('EVM')
a.geometry('600x600')
b=Label(a,text='BJP',font='timesnewroman 15 bold ',height=2,width=10,fg='black',bg='yellow')
b.place(x=20,y=20)
button1=Button(a,text='B1',font='timesnewroman 15 bold',height=1,width=10,fg='red',bg='yellow',activeforeground='blue',activebackground='pink',command=evm1)
button1.place(x=300,y=20)
c=Label(a,text='CONGRESS',font='timesnewroman 15 bold ',height=2,width=10,fg='black',bg='yellow')
c.place(x=20,y=90)
button2=Button(a,text='B2',font='timesnewroman 15 bold',height=1,width=10,fg='red',bg='yellow',activeforeground='blue',activebackground='pink',command=evm2)
button2.place(x=300,y=100)
d=Label(a,text='AAP',font='timesnewroman 15 bold ',height=2,width=10,fg='black',bg='yellow')
d.place(x=20,y=160)
button3=Button(a,text='B3',font='timesnewroman 15 bold',height=1,width=10,fg='red',bg='yellow',activeforeground='blue',activebackground='pink',command=evm3)
button3.place(x=300,y=180)
button4=Button(a,text='B4',font='timesnewroman 15 bold',height=1,width=10,fg='red',bg='yellow',activeforeground='blue',activebackground='pink',command=total)
button4.place(x=160,y=280)
