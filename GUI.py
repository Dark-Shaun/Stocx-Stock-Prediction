from tkinter import *
import tkinter as tk
from tkinter.ttk import Progressbar,Style
from PIL import ImageTk,Image
from name import *
from stock import *
from timestamp import *
from logo import *
HEIGHT=500
WIDTH=900


def func(entry_1,entry_2,label_22,label_9,label_19,label_20,label_21):
    ticker=entry_1
    no_of_days=entry_2
    company_name_1,ticker,company_name=symbol(ticker)
    label_22['text']=company_name
    a,b,c,predictions_1,predictions_2=predict(ticker,int(no_of_days))
    if len(predictions_2)==1:
        label_9['text']=predictions_1
    else:
        label_27['text']=predictions_2

    label_19['text']=a
    label_20['text']=b
    label_21['text']=c

    global name_1
    global image
    name_1=logo(company_name_1,ticker)
    image = PhotoImage(file=name_1)
    label_26=Label(frame,image=image)
    label_26.place(x=720,y=90)


def func_1(entry,entry_3,label_23,label_15,label_16,label_17,label_18):
    ticker=entry
    date=entry_3
    company_name_1,ticker,company_name=symbol(ticker)
    label_23['text']=company_name
    o,h,l,c=timestamp(ticker,date)
    label_15['text']=o
    label_16['text']=h
    label_17['text']=l
    label_18['text']=c
    global name_1
    global image
    name_1=logo(company_name_1,ticker)
    image = PhotoImage(file=name_1)
    label_26=Label(frame,image=image)
    label_26.place(x=720,y=90)






root=tk.Tk()
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH,bg='black',bd='10')
canvas.pack()

frame=tk.Frame(canvas,bg='#b8ffb5')
frame.place(x=12,y=12,height=500,width=900)
frame_1=tk.Frame(frame,bg='#000000')
frame_1.place(x=440,y=150,height=340,width=5)






label=tk.Label(frame,text='STOCX',font=('Balsamiq Sans',45),fg='black',bg='#b8ffb5')
label.place(x=345,y=50)
label_1=tk.Label(frame,text='Ticker Symbol:',font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_1.place(x=50,y=180)
label_2=tk.Label(frame,text='Ticker Symbol:',font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_2.place(x=475,y=180)
label_3=tk.Label(frame,text='Company:',font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_3.place(x=50,y=220)
label_4=tk.Label(frame,text='Company:',font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_4.place(x=475,y=220)
label_22=tk.Label(frame,font=('Balsamiq Sans',12),fg='black',bg='#ffffff')
label_22.place(x=160,y=225,height=20,width=270)
label_23=tk.Label(frame,font=('Balsamiq Sans',12),fg='black',bg='#ffffff')
label_23.place(x=585,y=225,height=20,width=300)
label_5=tk.Label(frame,text="No of Days:",font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_5.place(x=50,y=260)
label_25=tk.Label(frame,text="Open:",font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_25.place(x=50,y=290)
label_6=tk.Label(frame,text="High:",font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_6.place(x=50,y=320)
label_7=tk.Label(frame,text="Low:",font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_7.place(x=50,y=350)
label_8=tk.Label(frame,text="Predicted Closing Price:",font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_8.place(x=50,y=380)
label_9=tk.Label(frame,font=('Balsamiq Sans',10),fg='black',bg='#ffffff')
label_9.place(x=290,y=380,height=25,width=55)
label_10=tk.Label(frame,text="Timestamp:",font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_10.place(x=475,y=260)
label_19=tk.Label(frame,text="(yyyy-mm-dd)",font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_19.place(x=750,y=260)
label_11=tk.Label(frame,text="Open:",font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_11.place(x=475,y=290)
label_12=tk.Label(frame,text="High:",font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_12.place(x=475,y=320)
label_13=tk.Label(frame,text="Low:",font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_13.place(x=475,y=350)
label_14=tk.Label(frame,text="Close:",font=('Balsamiq Sans',15),fg='black',bg='#b8ffb5')
label_14.place(x=475,y=380)
label_15=tk.Label(frame,font=('Balsamiq Sans',10),fg='black',bg='#ffffff')
label_15.place(x=540,y=295,height=20,width=50)
label_16=tk.Label(frame,font=('Balsamiq Sans',10),fg='black',bg='#ffffff')
label_16.place(x=540,y=325,height=20,width=50)
label_17=tk.Label(frame,font=('Balsamiq Sans',10),fg='black',bg='#ffffff')
label_17.place(x=530,y=355,height=20,width=50)
label_18=tk.Label(frame,font=('Balsamiq Sans',10),fg='black',bg='#ffffff')
label_18.place(x=545,y=385,height=20,width=50)
label_19=tk.Label(frame,font=('Balsamiq Sans',10),fg='black',bg='#ffffff')
label_19.place(x=120,y=295,height=20,width=50)
label_20=tk.Label(frame,font=('Balsamiq Sans',10),fg='black',bg='#ffffff')
label_20.place(x=110,y=325,height=20,width=50)
label_21=tk.Label(frame,font=('Balsamiq Sans',10),fg='black',bg='#ffffff')
label_21.place(x=110,y=355,height=20,width=50)
label_27=tk.Label(frame,font=('Balsamiq Sans',10),fg='black',bg='#b8ffb5')
label_27.place(x=30,y=455,height=25,width=400)

###image work






entry=tk.Entry(frame)
entry.place(x=630,y=180,height=30,width=50)
entry_1=tk.Entry(frame)
entry_1.place(x=205,y=180,height=30,width=50)
entry_2=tk.Entry(frame)
entry_2.place(x=170,y=260,height=28,width=30)
entry_3=tk.Entry(frame)
entry_3.place(x=595,y=260,height=30,width=150)


button=Button(frame,text='Predict',fg='#111111',command=lambda:func(entry_1.get(),entry_2.get(),label_22,label_9,label_19,label_20,label_21))
button.place(x=180,y=415)
button_1=Button(frame,text='Check',fg='#111111',command=lambda:func_1(entry.get(),entry_3.get(),label_23,label_15,label_16,label_17,label_18))
button_1.place(x=650,y=410)



root.mainloop()
