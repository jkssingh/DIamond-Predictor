
class visual(object):
    def __init__(self,tab):
        self.tab=tab
    def phot(self):
        import tkinter as tk
        import diamond_photo_class as graph
        carat_price=graph.carat_price()
        cut_price=graph.cut_price() 
        color_price=graph.color_price()
        clarity_price=graph.clarity_price()
        depth_price=graph.depth_price() 
        table_price=graph.table_price()

        
        label11=tk.Label(self.tab,text='Visualization',justify=tk.CENTER,font=('Arial Bold Italic',40))
        label11.grid(column=0,row=0,columnspan=9)
        
        label12=tk.Label(self.tab,text='Carat vs Price',font=('Arial Bold Italic',20))
        label12.grid(column=0,row=1,ipadx=30)
        
        button=tk.Button(self.tab,text='Histogram',height=3,width=10,command=carat_price.hist)
        button.grid(column=0,row=2,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Scatterplot Colorless',height=3,width=10,command=carat_price.implot_colorless)            
        button.grid(column=0,row=3,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Scatterplot Color',height=3,width=10,command=carat_price.implot_color_color)
        button.grid(column=0,row=4,pady=20,ipadx=30)
        
        button=tk.Button(self.tab,text='Scatterplot Cut',height=3,width=10,command=carat_price.implot_color_cut)
        button.grid(column=0,row=5,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Scatterplot Clarity',height=3,width=10,command=carat_price.implot_color_clarity)
        button.grid(column=0,row=6,pady=20,ipadx=30)

        label13=tk.Label(self.tab,text='Cut vs Price',font=('Arial Bold Italic',20))
        label13.grid(column=1,row=1,ipadx=30)

        button=tk.Button(self.tab,text='Countplot',height=3,width=10,command=cut_price.countplot)
        button.grid(column=1,row=2,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Boxplot',height=3,width=10,command=cut_price.boxplot)
        button.grid(column=1,row=3,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Violinplot',height=3,width=10,command=cut_price.violinplot)
        button.grid(column=1,row=4,pady=20,ipadx=30)

        label14=tk.Label(self.tab,text='Color vs Price',font=('Arial Bold Italic',20))
        label14.grid(column=2,row=1,ipadx=30)

        button=tk.Button(self.tab,text='Countplot',height=3,width=10,command=color_price.countplot)
        button.grid(column=2,row=2,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Boxplot',height=3,width=10,command=color_price.boxplot)
        button.grid(column=2,row=3,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Violinplot',height=3,width=10,command=color_price.violinplot)
        button.grid(column=2,row=4,pady=20,ipadx=30)

        label15=tk.Label(self.tab,text='Clarity vs Price',font=('Arial Bold Italic',20))
        label15.grid(column=3,row=1,ipadx=30)

        button=tk.Button(self.tab,text='Countplot',height=3,width=10,command=clarity_price.countplot)
        button.grid(column=3,row=2,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Boxplot',height=3,width=10,command=clarity_price.boxplot)
        button.grid(column=3,row=3,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Violinplot',height=3,width=10,command=clarity_price.violinplot)
        button.grid(column=3,row=4,pady=20,ipadx=30)

        label16=tk.Label(self.tab,text='Depth vs Price',font=('Arial Bold Italic',20))
        label16.grid(column=4,row=1,ipadx=30)

        button=tk.Button(self.tab,text='Histogram',height=3,width=10,command=depth_price.hist)
        button.grid(column=4,row=2,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Scatterplot Colorless',height=3,width=10,command=depth_price.implot_colorless)
        button.grid(column=4,row=3,pady=20,ipadx=30)
        
        button=tk.Button(self.tab,text='Scatterplot Color',height=3,width=10,command=depth_price.implot_color_color)
        button.grid(column=4,row=4,pady=20,ipadx=30)
        
        button=tk.Button(self.tab,text='Scatterplot Cut',height=3,width=10,command=depth_price.implot_color_cut)
        button.grid(column=4,row=5,pady=20,ipadx=30)
        
        button=tk.Button(self.tab,text='Scatterplot Clarity',height=3,width=10,command=depth_price.implot_color_clarity)
        button.grid(column=4,row=6,pady=20,ipadx=30)
        
        label17=tk.Label(self.tab,text='Table vs Price',font=('Arial Bold Italic',20))
        label17.grid(column=5,row=1,ipadx=30)
        
        button=tk.Button(self.tab,text='Histogram',height=3,width=10,command=table_price.hist)
        button.grid(column=5,row=2,pady=20,ipadx=30)
        
        button=tk.Button(self.tab,text='Scatterplot Colorless',height=3,width=10,command=table_price.implot_colorless)
        button.grid(column=5,row=3,pady=20,ipadx=30)
        
        button=tk.Button(self.tab,text='Scatterplot Color',height=3,width=10,command=table_price.implot_color_color)
        button.grid(column=5,row=4,pady=20,ipadx=30)
        
        button=tk.Button(self.tab,text='Scatterplot Cut',height=3,width=10,command=table_price.implot_color_cut)
        button.grid(column=5,row=5,pady=20,ipadx=30)

        button=tk.Button(self.tab,text='Scatterplot Clarity',height=3,width=10,command=table_price.implot_color_clarity)
        button.grid(column=5,row=6,pady=20,ipadx=30)


