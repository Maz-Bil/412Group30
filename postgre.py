import psycopg2
import tkinter as tk
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

con = psycopg2.connect(
            host = "127.0.0.1",
            database = "project",
            user = "fdrobles",
            port = "8888"
)

cur = con.cursor()
cur.execute("select regionn, sum(dcount) from state join region on state.regionid = region.regionid group by regionn;")
rows = cur.fetchall()
df1 = pd.DataFrame(zip(*rows))
df1.columns = df1.iloc[0]
df1 = df1.drop(0)
df1 = df1.T

root = Tk()


figure2 = plt.figure(figsize=(10,10), dpi=95)
ax2 = figure2.add_subplot(111)
bar2 = FigureCanvasTkAgg(figure2, root)
bar2.get_tk_widget().pack(side=tk.BOTTOM, fill = tk.BOTH)
graph = df1.plot(kind='pie', legend = False, ax=ax2, subplots=True, autopct='%1.1f%%')
#graph.tick_params(axis='x', labelrotation = 90, labelsize = 6)
ax2.set_title('Test')
#ax1.set_xlabel('Regions')

figure1 = plt.figure(figsize=(10,10), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.BOTTOM, fill = tk.BOTH)
graph = df1.plot(kind='bar', legend = False, ax=ax1)
graph.tick_params(axis='x', labelrotation = 90, labelsize = 14)
ax1.set_title('Test')
ax1.set_xlabel('Regions')



options = [
    "Red",
    "Blue",
    "Orange",
    "Yellow",
    "Green",
    "Purple"
]

def currentQuery():
    if option.get() == "Red":
        colorB = "Red"
    elif option.get() == "Blue":
        colorB = "Blue"
    elif option.get() == "Orange":
        colorB = "Orange"
    elif option.get() == "Yellow":
        colorB = "Yellow"
    elif option.get() == "Green":
        colorB = "Green"
    elif option.get() == "Purple":
        colorB = "Purple"

    if region.get() == 1 and deaths.get() == 1 and state.get() != 1 and cases.get() != 1:
        ax1.clear()
        ax2.clear()
        cur.execute("select regionn, sum(dcount) from state join region on state.regionid = region.regionid group by regionn limit 100;")
        rows = cur.fetchall()
        df1 = pd.DataFrame(zip(*rows))
        df1.columns = df1.iloc[0]
        df1 = df1.drop(0)
        df1 = df1.T
        
        #print(df1.iloc[:,1])
        g = df1.plot(kind = 'bar',legend = False, ax=ax1, color = colorB)
        g.tick_params(axis='x', labelrotation = 90, labelsize = 14)
        g.tick_params(axis='y', labelsize = 14)
        g.ticklabel_format(style='plain', axis='y')
        ax1.set_title('Deaths per Region')
        ax1.set_xlabel('Regions')
        
        bar1.draw()

        #bar2.get_tk_widget().pack_forget()
        bar2.get_tk_widget().pack(side=tk.BOTTOM, fill = tk.BOTH)
        g = df1.plot(kind='pie', legend = False, ax=ax2, subplots=True, autopct='%1.1f%%')
        ax2.set_title('')
        bar2.draw()


    elif state.get() == 1 and deaths.get() == 1 and region.get() != 1 and cases.get() != 1:
        ax1.clear()
        ax2.clear()
        cur.execute("select statename, sum(dcount) from state group by statename;")
        rows = cur.fetchall()
        df1 = pd.DataFrame(zip(*rows))
        df1.columns = df1.iloc[0]
        df1 = df1.drop(0)
        df1 = df1.T
        g = df1.plot(kind='bar', legend = False, ax=ax1, color = colorB)
        g.tick_params(axis='x', labelrotation = 90, labelsize = 14)
        g.tick_params(axis='y', labelsize = 14)
        g.ticklabel_format(style='plain', axis='y')
        ax1.set_title('Deaths per State')
        ax1.set_xlabel('States')
        
        bar1.draw()


        #bar2.get_tk_widget().pack_forget()
        bar2.get_tk_widget().pack(side=tk.BOTTOM, fill = tk.BOTH)
        g = df1.plot(kind='pie', legend = False, ax=ax2, subplots=True, autopct='%1.1f%%')
        ax2.set_title('')
        bar2.draw()
    elif region.get() == 1 and cases.get() == 1 and state.get() != 1 and deaths.get() != 1:
        ax1.clear()
        ax2.clear()
        cur.execute("select regionn, sum(casenum) from state join region on state.regionid = region.regionid group by regionn;")
        rows = cur.fetchall()
        df1 = pd.DataFrame(zip(*rows))
        df1.columns = df1.iloc[0]
        df1 = df1.drop(0)
        df1 = df1.T
        g = df1.plot(kind='bar', legend = False, ax=ax1, color = colorB)
        g.tick_params(axis='x', labelrotation = 90, labelsize = 14)
        g.tick_params(axis='y', labelsize = 14)
        g.ticklabel_format(style='plain', axis='y')
        ax1.set_title('Cases per Region')
        ax1.set_xlabel('Regions')
        
        bar1.draw()


        #bar2.get_tk_widget().pack_forget()
        bar2.get_tk_widget().pack(side=tk.BOTTOM, fill = tk.BOTH)
        g = df1.plot(kind='pie', legend = False, ax=ax2, subplots=True, autopct='%1.1f%%')
        ax2.set_title('')
        bar2.draw()
    elif state.get() == 1 and cases.get() == 1 and region.get() != 1 and deaths.get() != 1:
        ax1.clear()
        ax2.clear()
        cur.execute("select statename, sum(casenum) from state group by statename;")
        rows = cur.fetchall()
        df1 = pd.DataFrame(zip(*rows))
        df1.columns = df1.iloc[0]
        df1 = df1.drop(0)
        df1 = df1.T
        g = df1.plot(kind='bar', legend = False, ax=ax1, color = colorB)
        g.tick_params(axis='x', labelrotation = 90, labelsize = 14)
        g.tick_params(axis='y', labelsize = 14)
        g.ticklabel_format(style='plain', axis='y')
        ax1.set_title('Cases per State')
        ax1.set_xlabel('States')
        
        bar1.draw()


        #bar2.get_tk_widget().pack_forget()
        bar2.get_tk_widget().pack(side=tk.BOTTOM, fill = tk.BOTH)
        g = df1.plot(kind='pie', legend = False, ax=ax2, subplots=True, autopct='%1.1f%%')
        ax2.set_title('')
        bar2.draw()

print(df1)

#ax1.set_xticklabels(rotation = 50)
#ax1.legend(df1, ['West', 'Southwest', 'Midwest', 'Southeast', 'Northeast'])
#plt.bar(*zip(*rows))
#plt.xticks(fontsize = 4, rotation = 90, ha = 'right')
#plt.show()

region = IntVar()
state = IntVar()
cases = IntVar()
deaths = IntVar()

button1 = tk.Checkbutton(root, text="Region", height=3, width=10, font=20, variable = region, command=currentQuery).place(x=1600, y=30)
#button1.pack(side=Tk.LEFT, fill = Tk.BOTH)
button2 = tk.Checkbutton(root, text="State", height=3, width=10, font=20, variable = state, command=currentQuery).place(x=1800, y=30)
#button2.pack(side=Tk.LEFT, fill=Tk.BOTH)
button3 = tk.Checkbutton(root, text="Cases", height=3, width=10, font=20, variable = cases, command=currentQuery).place(x=2000, y=30)
#button3.pack(side=Tk.LEFT, fill=Tk.BOTH)
button4 = tk.Checkbutton(root, text="Deaths", height=3, width=10, font=20, variable = deaths, command=currentQuery).place(x=2200, y=30)
#button4.pack(side=Tk.LEFT, fill=Tk.BOTH)
option = StringVar()
option.set("Red")
drop = OptionMenu(root, option, *options).place(x=2400,y=30)

root.mainloop()


cur.close()

con.close()