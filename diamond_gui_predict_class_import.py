class predict_price(object):
    def __init__(self,tab):
        self.tab=tab
    def price(self):
        import tkinter as tk
        import pickle
        import pandas as pd
        file=open('reg.txt','rb')
        file3=open('reg_encod.txt','rb')
        file4=open('reg_scaler.txt','rb')
        reg=pickle.load(file)
        encoder=pickle.load(file3)
        scaler=pickle.load(file4)
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
            if e1.get() !='' and e5.get() !='' and e6.get() !='' and e7.get() !='' and e8.get() !='' and e9.get() !='' :
                carat,cut,color,clarity=float(e1.get()),e2.get().strip(),e3.get().strip(),e4.get().strip()
                depth,table=float(e5.get()),float(e6.get())
                x,y,z=float(e7.get()),float(e8.get()),float(e9.get())
                area=x*y*z
                X_debug={'carat':[carat],'cut':[cut],'color':[color],'clarity':[clarity],
                         'depth':[depth],'table':[table],'volume':[area]}
                X_debug=pd.DataFrame(data=X_debug)
                X_debug=X_debug.iloc[:,:].values
                X_debug[:,1]=encoder[0].transform(X_debug[:,1])
                X_debug[:,2]=encoder[1].transform(X_debug[:,2])
                X_debug[:,3]=encoder[2].transform(X_debug[:,3])
                X_debug=encoder[3].transform(X_debug).toarray().reshape(1,-1)
                X_debug=X_debug[:,1:27]
                if(e10.get()=='Support Vector Machine'):
                    X_debug=scaler[0].transform(X_debug)
                    value=reg_dic[e10.get()].predict(X_debug)
                    value=scaler[1].inverse_transform(value)
                else:
                    value=reg_dic[e10.get()].predict(X_debug)
                label11.configure(text=value)
            else:
                label11.configure(text='Enter the Required Value\'s')
                
        label=tk.Label(self.tab,text='Price',font=('Arial Bold Italic',40))
        label.grid(column=0,row=0,columnspan=2)
        reg=self.tab.register(correct)
        
        label1=tk.Label(self.tab,text='Carat',font=('Arial Bold',20))
        label1.grid(column=0,row=1,padx=10,pady=10)
        e1=tk.Entry(self.tab,font=('Arial Bold',20),cursor='pencil')
        e1.grid(row=1,column=1)
        e1.config(validate='key',validatecommand=(reg,'%P','%d'))
        
        label2=tk.Label(self.tab,text='Cut',font=('Arial Bold',20))
        label2.grid(column=0,row=2,padx=10,pady=10)
        cut=['Fair','Good','Ideal','Premium','Very Good']
        e2=tk.StringVar()
        e2.set('Very Good')
        popupmenu=tk.OptionMenu(self.tab,e2,*cut)
        popupmenu.configure(activebackground='#cecece',cursor='hand2',font=('Arial Bold',10))
        popupmenu.grid(row=2,column=1,sticky='ew',ipadx=10,pady=10)
        
        
        label3=tk.Label(self.tab,text='Color',font=('Arial Bold',20))
        label3.grid(column=0,row=3,padx=10,pady=10)
        color=['D','E','F','G','H','I','J']
        e3=tk.StringVar()
        e3.set('E')
        popupmenu=tk.OptionMenu(self.tab,e3,*color)
        popupmenu.configure(activebackground='#cecece',cursor='hand2',font=('Arial Bold',10))
        popupmenu.grid(row=3,column=1,sticky='ew')

        label4=tk.Label(self.tab,text='Clarity',font=('Arial Bold',20))
        label4.grid(column=0,row=4,padx=10,pady=10)
        clarity=['I1','IF','SI1','SI2','VS1','VS2','WS1']
        e4=tk.StringVar()
        e4.set('SI1')
        popupmenu=tk.OptionMenu(self.tab,e4,*clarity)
        popupmenu.configure(activebackground='#cecece',cursor='hand2',font=('Arial Bold',10))
        popupmenu.grid(row=4,column=1,sticky='ew')

        label5=tk.Label(self.tab,text='Depth',font=('Arial Bold',20))
        label5.grid(column=0,row=5,padx=10,pady=10)
        e5=tk.Entry(self.tab,font=('Arial Bold',20),cursor='pencil')
        e5.grid(row=5,column=1)
        e5.config(validate='key',validatecommand=(reg,'%P','%d'))

        label6=tk.Label(self.tab,text='Table',font=('Arial Bold',20))            
        label6.grid(column=0,row=6,padx=10,pady=10)
        e6=tk.Entry(self.tab,font=('Arial Bold',20),cursor='pencil')
        e6.grid(row=6,column=1)
        e6.config(validate='key',validatecommand=(reg,'%P','%d'))

        label7=tk.Label(self.tab,text='X',font=('Arial Bold',20))
        label7.grid(column=0,row=7,padx=10,pady=10)
        e7=tk.Entry(self.tab,font=('Arial Bold',20),cursor='pencil')
        e7.grid(row=7,column=1)
        e7.config(validate='key',validatecommand=(reg,'%P','%d'))

        label8=tk.Label(self.tab,text='Y',font=('Arial Bold',20))
        label8.grid(column=0,row=8,padx=10,pady=10)
        e8=tk.Entry(self.tab,font=('Arial Bold',20),cursor='pencil')
        e8.grid(row=8,column=1)
        e8.config(validate='key',validatecommand=(reg,'%P','%d'))

        label9=tk.Label(self.tab,text='Z',font=('Arial Bold',20))
        label9.grid(column=0,row=9,padx=10,pady=10)
        e9=tk.Entry(self.tab,font=('Arial Bold',20),cursor='pencil')
        e9.grid(row=9,column=1)
        e9.config(validate='key',validatecommand=(reg,'%P','%d'))

        label10=tk.Label(self.tab,text='Prediction Algo',font=('Arial Bold',20))
        label10.grid(column=0,row=10,padx=10,pady=10)
        algo=['Linear Regression','Support Vector Machine','Lasso Regression','Ridge Regression','Ada Boosting',
              'Gradient Boosting','Decision Tree','Random Forest']
        e10=tk.StringVar()
        e10.set('Linear Regression')
        popupmenu=tk.OptionMenu(self.tab,e10,*algo)
        popupmenu.configure(activebackground='#cecece',cursor='hand2',font=('Arial Bold',10))
        popupmenu.grid(column=1,row=10,sticky='ew',ipadx=10,pady=10)

        button=tk.Button(self.tab,text='Calculate',justify=tk.CENTER,height=3,width=10,command=predict)
        button.configure(cursor='hand2')
        button.grid(column=0,row=11,columnspan=2,padx=10,ipadx=30)
        
        label11=tk.Label(self.tab,font=('Arial Bold',20))
        label11.grid(column=0,row=12,sticky='W',padx=10,pady=10,columnspan=2)
        
    
