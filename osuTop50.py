# osuTop50

from tkinter import *
import tkinter.ttk as ttk
from tkinter import scrolledtext

#list of full country names and their codes
countries = {
    'AU': 'AUSTRALIA',
    'GB': 'UNITED KINGDOM',
    'PL': 'POLAND',
    'ID': 'INDONESIA',
    'US': 'UNITED STATES',
    'NO': 'NORWAY',
    'RU': 'RUSSIA',
    'BR': 'BRAZIL',
    'ES': 'SPAIN',
    'KR': 'SOUTH KOREA',
    'DE': 'GERMANY',
    'PH': 'PHILIPPINES',
    'AE': 'UNITED ARAB EMIRATES',
    'NZ': 'NEW ZEALAND',
    'MY': 'MALAYSIA',
    'RO': 'ROMANIA',
    'AR': 'ARGENTINA',
    'CL': 'CHILE',
    'CA': 'CANADA',
    'JP': 'JAPAN',
    'TH': 'THAILAND',
    'KZ': 'KAZAKHSTAN',
    'VN': 'VIETNAM',
    'BE': 'BELGIUM',
    'QA': 'QATAR',
    'PE': 'PERU',
    'NL': 'NETHERLANDS',
    'PT': 'PORTUGAL',
    'LV': 'LATVIA',
    'JE': 'JERSEY',
    'SE': 'SWEDEN',
    'HK': 'HONG KONG',
    'TR': 'TURKEY',
    'AT': 'AUSTRIA',
    'EC': 'ECUADOR',
    'MA': 'MOROCCO',
    'LT': 'LITHUANIA',
    'RS': 'SERBIA',
    'FR': 'FRANCE',
    'MX': 'MEXICO',
    'EE': 'ESTONIA',
    'SG': 'SINGAPORE',
    'TW': 'TAIWAN'
}

def clicked():
    display.config(state=NORMAL)
    #sets up the file name
    year = comboBox2.get()
    file = f"osu-archive-{year}.csv"
    #Filters out the rank range
    box1 = rankBox1.get()
    box2 = rankBox2.get()   
    if box1.isdigit() and int(box1) > 0 and box2.isdigit() and int(box2) > int(box1):
        first = rankBox1.get()
        last = rankBox2.get()
    # Gets the country the user searched entered
    code = ""
    for key, value in countries.items():
        if countryBox.get().upper() == key or countryBox.get().upper() == value:
            code = key
            
    #deletes previous displayed data
    display.delete(0.0, END)
    display.insert(INSERT,"Rank	Name		Country		PP\n")
    
    with open(file, "r") as file:
        next(file)
        #checks what order to display in
        data = file.readlines()
        if comboBox1.get() == "Low to High":
            data.reverse()
        #Displays the data
        for line in data:
            data = line.split(",")
            if int(data[0][1:]) > int(box1) - 1 and int(data[0][1:]) < int(box2) + 1:
                #checks if a country is being filtered
                if code == data[1][-2:]:
                    pp = f"{data[4]},{data[5]}".replace('"',"")
                    display.insert(INSERT, f"{data[0]}".ljust(8)+ f"{data[2]}".ljust(16)+ f"{data[1][-2:]}".ljust(16) + pp)
                elif code == "":
                    pp = f"{data[4]},{data[5]}".replace('"',"")
                    display.insert(INSERT, f"{data[0]}".ljust(8)+ f"{data[2]}".ljust(16)+ f"{data[1][-2:]}".ljust(16) + pp)
                elif code == "a":
                    display.insert(INSERT, f"Non applicable country")
                    break
                    

    display.config(state=DISABLED)
    
# saves displayed text as file
def save():
    saveData = display.get("1.0", END)
    with open("data.txt", "w") as file:
        file.write(saveData)
#loads the previous save
def load():
    with open("data.txt", "r") as file:
        display.config(state=NORMAL)
        display.delete(0.0, END)
        for line in file:
            display.insert(INSERT,line)
        display.config(state=DISABLED)
            
window = Tk()
window.iconbitmap("osu.ico")
window.title("Osu Database")
window.geometry('640x420')
window.configure(bg = "#1d1719")
window.resizable(False,False)
photo = PhotoImage(file="banner.png")
img = Label(window, image = photo, bd = 0)
img.place(x=0,y=-165)
frame = Frame(window)
frame.configure(bg = "#1d1719")
img = Label(frame, image = photo, bd = 0)
img.place(x=0,y=-165)
countryTxt = Label(frame, text="Country", bg = "#2c2226", fg = "#cd9486")
countryTxt.grid(row=0, column=0,columnspan = 4)
countryBox = Entry(frame,width=20,bg = "#2c2226", fg = "#cd9486")
countryBox.grid(row=1, column= 0, columnspan = 4)

back = PhotoImage(file = "banner.png")

filterTxt1 = Label(frame, text="Order", bg = "#2c2226", fg = "#cd9486")
filterTxt1.grid(row=2, column=0)
filterTxt2 = Label(frame, text="Year", bg = "#2c2226", fg = "#cd9486")
filterTxt2.grid(row=2, column=3)

rankTxt = Label(frame, text="Rank Range (1-50)", bg = "#2c2226", fg = "#cd9486")
rankTxt.grid(row=2, columnspan = 4)

# creates the entry boxes and sets their default values
v1 = IntVar()
rankBox1 = Entry(frame, width = 20, text = v1, bg = "#2c2226", fg = "#cd9486")
v1.set(1)
rankBox1.grid(row=3, column = 1)
v2 = IntVar()
rankBox2 = Entry(frame, width = 20, text = v2, bg = "#2c2226", fg = "#cd9486")
v2.set(50)
rankBox2.grid(row=3, column = 2)

comboBox1 = ttk.Combobox(frame, width = 11, state = "readonly")
comboBox1.grid(row=3, column = 0)
comboBox1['values'] = ["High to Low", "Low to High"]
comboBox1.current(0)

comboBox2 = ttk.Combobox(frame, width = 11, state = "readonly")
comboBox2.grid(row=3, column = 3)
comboBox2['values'] = ["2025","2024","2023","2022","2021","2020","2019"]
comboBox2.current(0)

updateBtn = Button(frame, text="Update", command = clicked, bg = "#49393f")
updateBtn.grid(row=4, column=0, columnspan = 4)

saveBtn = Button(frame, text="Save", command = save, bg = "#49393f")
saveBtn.grid(row=6,column=1)
loadBtn = Button(frame, text="Load", command = load, bg = "#49393f")
loadBtn.grid(row=6, column=2)

display = scrolledtext.ScrolledText(frame,width=52,height=13, bg = "#2c2226", fg = "#cd9486")

display.grid(row=5,columnspan = 4)

counter = 0

frame.pack(anchor = CENTER)
window.mainloop()
