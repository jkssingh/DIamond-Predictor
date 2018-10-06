import tkinter as tk
import pickle
import pandas as pd
file=open('reg.txt','rb')
file2=open('reg_score.txt','rb')
file3=open('reg_encod.txt','rb')
reg=pickle.load(file)
score=pickle.load(file2)
encoder=pickle.load(file3)
X_debug={}

reg_dic={'Linear Regression':reg[0],'Support Vector Machine':reg[1],'Lasso Regression':reg[2],
            'Ridge Regression':reg[3],'Ada Boosting':reg[4],'Gradient Boosting':reg[5],
            'Decision Tree':reg[6],'Random Forest':reg[7]}
def correct(inp,type):
    try:
        if(type== '1' ):
            if inp.find(' ') == -1:
                inp=float(inp.strip())
                return True
            else:
                return False
        elif(type== '0'):
            return True
    except ValueError:
        return False
    
def predict():
    global X_debug,reg_dic
    if e1.get() !='' and e5.get() !='' and e6.get() !='' and e7.get() !='' and e8.get() !='' and e9.get() !='' :
        carat,cut,color,clarity=float(e1.get()),e2.get().strip(),e3.get().strip(),e4.get().strip()
        depth,table=float(e5.get()),float(e6.get())
        x,y,z=float(e7.get()),float(e8.get()),float(e9.get())
        X_debug={'carat':[carat],'cut':[cut],'color':[color],'clarity':[clarity],
             'depth':[depth],'table':[table],'x':[x],'y':[y],'z':[z]}
        X_debug=pd.DataFrame(data=X_debug)
        X_debug=X_debug.iloc[:,:].values
        X_debug[:,1]=encoder[0].transform(X_debug[:,1])
        X_debug[:,2]=encoder[1].transform(X_debug[:,2])
        X_debug[:,3]=encoder[2].transform(X_debug[:,3])
        X_debug=encoder[3].transform(X_debug).toarray().reshape(1,-1)
        X_debug=X_debug[:,1:27]
        value=reg_dic[e10.get()].predict(X_debug)
        label10.configure(text=value)
    else:
        label10.configure(text=reg_dic[e10.get()])

window=tk.Tk()
window.title('Price Prediction of Diamond and Visualizing Diamond Dataset')
window.resizable(0,0)

frame=tk.Frame(window)
frame2=tk.Frame(window)

label=tk.Label(frame,text='Price',font=('Arial Bold Italic',40))
label.grid(column=0,row=0,columnspan=2)

#label10=tk.Label(frame2,text='Price',font=('Arial Bold Italic',20))
#label10.grid(column=0,row=0,sticky='W')
#
#label11=tk.Label(frame2,text='Vizualize',font=('Arial Bold Italic',20))
#label11.grid(column=0,row=1,sticky='W')
reg=window.register(correct)

label1=tk.Label(frame,text='Carat',font=('Arial Bold',20))
label1.grid(column=0,row=1,sticky='W',padx=10,pady=10)
e1=tk.Entry(frame,font=('Arial Bold',20))
e1.grid(row=1,column=1)
e1.config(validate='key',validatecommand=(reg,'%P','%d'))

label2=tk.Label(frame,text='Cut',font=('Arial Bold',20))
label2.grid(column=0,row=2,sticky='W',padx=10,pady=10)
cut=['Fair','Good','Ideal','Premium','Very Good']
e2=tk.StringVar()
e2.set('Very Good')
popupmenu=tk.OptionMenu(frame,e2,*cut)
popupmenu.configure(activebackground='#000000',font=('Arial Bold',10))
popupmenu.grid(row=2,column=1,sticky='ew',ipadx=10,pady=10)


label3=tk.Label(frame,text='Color',font=('Arial Bold',20))
label3.grid(column=0,row=3,sticky='W',padx=10,pady=10)
color=['D','E','F','G','H','I','J']
e3=tk.StringVar()
e3.set('E')
popupmenu=tk.OptionMenu(frame,e3,*color)
popupmenu.configure(activebackground='#000000',font=('Arial Bold',10))
popupmenu.grid(row=3,column=1,sticky='ew')

label4=tk.Label(frame,text='Clarity',font=('Arial Bold',20))
label4.grid(column=0,row=4,sticky='W',padx=10,pady=10)
clarity=['I1','IF','SI1','SI2','VS1','VS2','WS1']
e4=tk.StringVar()
e4.set('SI1')
popupmenu=tk.OptionMenu(frame,e4,*clarity)
popupmenu.configure(activebackground='#000000',font=('Arial Bold',10))
popupmenu.grid(row=4,column=1,sticky='ew')

label5=tk.Label(frame,text='Depth',font=('Arial Bold',20))
label5.grid(column=0,row=5,sticky='W',padx=10,pady=10)
e5=tk.Entry(frame,font=('Arial Bold',20))
e5.grid(row=5,column=1)
e5.config(validate='key',validatecommand=(reg,'%P','%d'))

label6=tk.Label(frame,text='Table',font=('Arial Bold',20))
label6.grid(column=0,row=6,sticky='W',padx=10,pady=10)
e6=tk.Entry(frame,font=('Arial Bold',20))
e6.grid(row=6,column=1)
e6.config(validate='key',validatecommand=(reg,'%P','%d'))

label7=tk.Label(frame,text='X',font=('Arial Bold',20))
label7.grid(column=0,row=7,sticky='W',padx=10,pady=10)
e7=tk.Entry(frame,font=('Arial Bold',20))
e7.grid(row=7,column=1)
e7.config(validate='key',validatecommand=(reg,'%P','%d'))

label8=tk.Label(frame,text='Y',font=('Arial Bold',20))
label8.grid(column=0,row=8,sticky='W',padx=10,pady=10)
e8=tk.Entry(frame,font=('Arial Bold',20))
e8.grid(row=8,column=1)
e8.config(validate='key',validatecommand=(reg,'%P','%d'))

label9=tk.Label(frame,text='Z',font=('Arial Bold',20))
label9.grid(column=0,row=9,sticky='W',padx=10,pady=10)
e9=tk.Entry(frame,font=('Arial Bold',20))
e9.grid(row=9,column=1)
e9.config(validate='key',validatecommand=(reg,'%P','%d'))

label10=tk.Label(frame,text='Prediction Algo',font=('Arial Bold',20))
label10.grid(column=0,row=10,sticky='W',padx=10,pady=10)
algo=['Linear Regression','Support Vector Machine','Lasso Regression','Ridge Regression','Ada Boosting',
     'Gradient Boosting','Decision Tree','Random Forest']
e10=tk.StringVar()
e10.set('Linear Regression')
popupmenu=tk.OptionMenu(frame,e10,*algo)
popupmenu.configure(activebackground='#000000',font=('Arial Bold',10))
popupmenu.grid(column=1,row=10,sticky='ew',ipadx=10,pady=10)

button=tk.Button(frame,text='Calculate',justify=tk.CENTER,height=3,width=10,command=predict)
button.grid(column=0,row=11,columnspan=2,padx=10,ipadx=30)

label10=tk.Label(frame,font=('Arial Bold',20))
label10.grid(column=0,row=12,sticky='W',padx=10,pady=10,columnspan=2)

frame.grid_columnconfigure(0,pad=30)
frame.grid(column=0,row=0,sticky='W',padx=20,pady=10)
frame2.grid(column=1,row=0,sticky='N')

window.geometry("800x1000")
window.mainloop()
