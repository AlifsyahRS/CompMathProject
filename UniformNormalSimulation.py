import numpy as np
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import norm
from scipy.stats import uniform



root = tk.Tk()
root.title("Uniform and Normal Distribution")
graphFrame = tk.Frame(root)

buttons_frame = tk.Frame(root)
tabControl = ttk.Notebook(buttons_frame)

#Formula for distributions
uniformf = lambda a,b: 1 / (b-a) # Formula for uniform distribution
normalf = lambda c,mu,std: (1 / (std * np.sqrt(2 * np.pi))) * np.exp( -0.5 * (c - mu / std) ** 2) #Formula for nomral distribution


#Functions

def normalPdf(c,mean,std):
    return normalf(c,mean,std)

def uniformPdf(c,a,b):
    if c>=a or c<=b:
        return uniformf(a,b)
    else:
        return 0

def normalCdf(c,mean,std):
    return norm.cdf(c, mean, std)

def uniformCdf(c,a,b):
    return uniform.cdf(c, a, b)




# Four Tkinter string variables to get the values from the entry widgets (a and b in normal distribution will represent the mean and standard deviation respectively)
aVar = tk.StringVar()
bVar = tk.StringVar()
cVar = tk.StringVar()
dVar = tk.StringVar()


#Uniform Probability Distribution Tab
showGraphUpd = tk.IntVar() # Variable to see if Checkbutton widget is active or not.
tabUpd = tk.Frame(tabControl)
tk.Label(tabUpd,text="X ~ U(a,b)").grid(row=0)
tk.Label(tabUpd,text="P(X = C), P(X) = (b + a) / 2").grid(row=1)
tk.Label(tabUpd,text="Lower Boundary (a)").grid(row=2)
tk.Label(tabUpd,text="Upper Boundary (b)").grid(row=3)
tk.Label(tabUpd,text="C").grid(row=4)
entryAUpd = tk.Entry(tabUpd,textvariable=aVar).grid(row=2,column=1)
entryBUpd = tk.Entry(tabUpd,textvariable=bVar).grid(row=3,column=1)
entryCUpd = tk.Entry(tabUpd,textvariable=cVar).grid(row=4,column=1)
checkButtonUpd = tk.Checkbutton(tabUpd,text="Show Graph",variable=showGraphUpd,onvalue=1,offvalue=0).grid(row=5,column=1)

def calcUpd():
    c = int(cVar.get())
    a = int(aVar.get())
    b = int(bVar.get())
    calcResult = uniformPdf(c,a,b)
    tk.Label(tabUpd,text=f"Calculated  results: {calcResult}").grid(row=8,column=1)
    for widgets in graphFrame.winfo_children():
        widgets.destroy()
    #Creating the figure for the graphs
    fig = plt.figure(111)
    plt.clf()
    ax = fig.add_subplot(111)
    if showGraphUpd.get() == 1:
        x = np.linspace(a,b,1000)
        y = np.zeros(x.shape[0])
        y = y+uniformf(a,b)
        ax.set_title("Uniform Probabilty Distribution")
        ax.plot(x,y)
        ax.plot(c,calcResult,'o',label="C")
        graph = FigureCanvasTkAgg(fig,graphFrame)
        ax.legend()
        graph.get_tk_widget().pack()
    
updCalcButton = tk.Button(tabUpd,text="Calculate",command=calcUpd).grid(row=7,column=1)

#Uniform Continuous Distribution Tab
showGraphUcd = tk.IntVar()
tabUcd = tk.Frame(tabControl)
tk.Label(tabUcd,text="X ~ U(a,b)").grid(row=0)
tk.Label(tabUcd,text="P(C < X < D), P(X) = (b + a) / 2").grid(row=1)
tk.Label(tabUcd,text="Lower Boundary (a)").grid(row=2)
tk.Label(tabUcd,text="Upper Boundary (b)").grid(row=3)
tk.Label(tabUcd,text="C").grid(row=4)
tk.Label(tabUcd,text="D").grid(row=5)
entryAUcd = tk.Entry(tabUcd,textvariable=aVar).grid(row=2,column=1)
entryBUcd = tk.Entry(tabUcd,textvariable=bVar).grid(row=3,column=1)
entryCUcd = tk.Entry(tabUcd,textvariable=cVar).grid(row=4,column=1)
entryDUcd = tk.Entry(tabUcd,textvariable=dVar).grid(row=5,column=1)
checkButtonUcd = tk.Checkbutton(tabUcd,text="Show Graph",variable=showGraphUcd,onvalue=1,offvalue=0).grid(row=6,column=1)

def calcUcd():
    c = int(cVar.get())
    d = int(dVar.get())
    a = int(aVar.get())
    b = int(bVar.get())
    calcResult = uniformCdf(d,a,b) - uniformCdf(c,a,b)
    tk.Label(tabUcd,text=f"Calculated  results: {calcResult}").grid(row=8,column=1)
    for widgets in graphFrame.winfo_children():
        widgets.destroy()
    #Creating the figure for the graphs
    fig = plt.figure(111)
    plt.clf()
    ax = fig.add_subplot(111)
    if showGraphUcd.get() == 1:
        x = np.linspace(a,b,1000)
        xfill = [c,d]
        y = np.zeros(x.shape[0])
        y = y+uniformf(a,b)
        ax.set_title("Uniform Continuous Distribution")
        ax.plot(x,y)
        ax.plot(c,uniformf(a,b),'o--',label="C")
        ax.plot(d,uniformf(a,b),'o--',label="D")
        ax.fill_between(xfill, uniformf(a,b), alpha = 0.5)
        ax.legend()
        graph = FigureCanvasTkAgg(fig,graphFrame)
        graph.get_tk_widget().pack()

ucdCalcButton = tk.Button(tabUcd,text="Calculate",command=calcUcd).grid(row=7,column=1)


# Normal Probabability Distribution Tab 
showGraphNpd = tk.IntVar()
tabNpd = tk.Frame(tabControl)
tk.Label(tabNpd,text="X ~ N(μ,σ)").grid(row=0)
tk.Label(tabNpd,text="P(X = C)").grid(row=1)
tk.Label(tabNpd, text="C").grid(row=2)
tk.Label(tabNpd, text="Mean (μ)").grid(row=3)
tk.Label(tabNpd, text="Standard Deviation (σ)").grid(row=4)
entryCNpd = tk.Entry(tabNpd,textvariable=cVar).grid(row=2,column=1)
entryMeanNpd = tk.Entry(tabNpd,textvariable=aVar).grid(row=3,column=1)
entryStdNpd= tk.Entry(tabNpd,textvariable=bVar).grid(row=4,column=1)
checkButtonNpd = tk.Checkbutton(tabNpd,text="Show Graph",variable=showGraphNpd,onvalue=1,offvalue=0).grid(row=5,column=1)

def calcNpd():
    
    c = int(cVar.get())
    mean = float(aVar.get())
    std = float(bVar.get())
    tk.Label(tabNpd,text=f"Calculated results: {normalPdf(c,mean,std)}").grid(row=7,column=1)
    for widgets in graphFrame.winfo_children():
        widgets.destroy()
    #Creating the figure for the graphs
    fig = plt.figure(111)
    plt.clf()
    ax = fig.add_subplot(111)
    if showGraphNpd.get() == 1:
        x = np.linspace(c-10,c+10,1000)
        ax.set_title("Normal Probability Distribution")
        ax.plot(x,normalf(x,mean,std))
        ax.plot(c,normalf(c,mean,std),'o',label="P(X=C)")
        ax.legend()
        graph = FigureCanvasTkAgg(fig,graphFrame)
        graph.get_tk_widget().pack()
    
npdCalcButton = tk.Button(tabNpd,text="Calculate",command=calcNpd).grid(row=6,column=1)




# Normal Continuous Distribution Function Tab 
showGraphNcd = tk.IntVar()
tabNcd = tk.Frame(tabControl)
tk.Label(tabNcd, text="X ~ N(μ,σ)").grid(row=0)
tk.Label(tabNcd,text="P(C < X < D)").grid(row=1)
tk.Label(tabNcd, text="C").grid(row=2)
tk.Label(tabNcd, text="D").grid(row=3)
tk.Label(tabNcd, text="Mean (μ)").grid(row=4)
tk.Label(tabNcd, text="Standard Devation (σ)").grid(row=5)
entryCNcd = tk.Entry(tabNcd,textvariable=cVar).grid(row=2,column=1)
entryDNcd = tk.Entry(tabNcd,textvariable=dVar).grid(row=3,column=1)
entryMeanNcd = tk.Entry(tabNcd,textvariable=aVar).grid(row=4,column=1)
entryStdNcd = tk.Entry(tabNcd,textvariable=bVar).grid(row=5,column=1)
checkButtonNcd = tk.Checkbutton(tabNcd,text="Show Graph",variable=showGraphNcd,onvalue=1,offvalue=0).grid(row=6,column=1)


def calcNcd():
    c = int(cVar.get())
    d = int(dVar.get())
    mean = float(aVar.get())
    std = float(bVar.get())
    calcResult = normalCdf(d,mean,std) - normalCdf(c,mean,std)
    tk.Label(tabNcd,text=f"Calculated results: {calcResult}").grid(row=8,column=1)
    for widgets in graphFrame.winfo_children():
        widgets.destroy()
    #Creating the figure for the graphs
    fig = plt.figure(111)
    plt.clf()
    ax = fig.add_subplot(111)
    if showGraphNcd.get() == 1:
        x = np.linspace(c-10,d+10,10000)
        xfill = np.linspace(c,d,1000)
        ax.set_title("Normal Continuous Distribution")
        ax.plot(x,normalf(x,mean,std))
        ax.plot(c,normalf(c,mean,std),'o--',label="C")
        ax.plot(d,normalf(d,mean,std),'o--',label="D")
        ax.fill_between(xfill,normalf(xfill,mean,std),alpha=0.5)
        ax.legend()
        graph = FigureCanvasTkAgg(fig,graphFrame)
        graph.get_tk_widget().pack()

        
    

ncdCalcButton= tk.Button(tabNcd,text="Calculate",command=calcNcd).grid(row=7,column=1)



#Adding all the tabs
tabControl.add(tabUpd,text="Uniform PDF")
tabControl.add(tabUcd,text="Uniform CDF")
tabControl.add(tabNpd,text="Normal PDF")
tabControl.add(tabNcd,text="Normal CDF")
tabControl.pack()



graphFrame.pack(side=tk.LEFT) # Graph will appear at the left side of the GUI.
buttons_frame.pack(side=tk.RIGHT) # Buttons and entry widgets will appear on the right.



root.mainloop()





