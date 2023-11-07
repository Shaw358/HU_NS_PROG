from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import UserWindow
from datetime import datetime
import datetime
import csv
import os
import DatabaseManager

# Tkinter init
window = Tk()

# Global Vars
max_characters = 140
nameFieldCleared = False
mainFieldCleared = False


# ---------------------------------------------------------------------------------------------------------------------------

# Pre Init functions
# FIXME: This is a stupid way of doing this, one function should be able to clear any text!
def ClearNameTextField(event):
    if not UserWindow.nameFieldCleared:
        UserWindow.nameFieldCleared = True
        name.delete("1.0", "end")


def ClearMainText_TextField(event):
    if not UserWindow.mainFieldCleared:
        UserWindow.mainFieldCleared = True
        mainText.delete("1.0", "end")


def OnTextFieldAltered(event):
    text = mainText.get("1.0", 'end-1c')
    length = len(text)
    if length > UserWindow.max_characters:
        charactersUsed.config(fg="red")
    else:
        charactersUsed.config(fg="black")
    charactersUsed.config(text=(str(length) + "/" + str(max_characters)))


# Helper functions
def DateGrabber():
    return datetime.datetime.today().replace(microsecond=0)


# NOTE: DEPRECATED
def WriteMessageToCSV(data):
    if data[0] is None or data[0] == "":
        data[0] = "Annoniem"

    with open('messages.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # NOTE: data[0] is the name, data[1] is the main message, data[2] is the station
        writer.writerow([DateGrabber(), data[0], data[1], data[2]])


def SubmitReview():
    query = "INSERT INTO Bericht (Bericht, _DateTime, ReizigerNaam, Station) VALUES (%s, %s, %s, %s);"
    params = (mainText.get("1.0", 'end-1c'), DateGrabber(), name.get("1.0", 'end-1c'), str(stationSelection.get()))
    text = mainText.get("1.0", 'end-1c')
    length = len(text)
    if length > UserWindow.max_characters or stationSelection.get() == "" or stationSelection.get() is None:
        a = 0
        # they fucked up
    else:
        DatabaseManager.ExecuteSQL_Query(query, params, False)


# creates the CSV if none exists - DEPRECATED
def CSV_Creator():
    if not os.path.isfile('messages.csv'):
        with open('messages.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)

            data = ["DateTime", "User", "Message", "Station", "ModerationResult", "ModerationDate",
                    "ModerationTime", "ModeratorName", "ModeratorEmail"]
            csv_writer.writerow(data)


# ---------------------------------------------------------------------------------------------------------------------------

# Never make me do UI code again please
window.geometry("1400x800")
window.resizable(False, False)

# background
background = ImageTk.PhotoImage(Image.open("Images/bg.jpg"))
backgroundPanel = Label(window, image=background)
backgroundPanel.place(x=0, y=0)

# Yellow Top Bar
topBarBg = ImageTk.PhotoImage(Image.open("Images/YB.png"))
topBarBgPanel = Label(window, image=topBarBg)
topBarBgPanel.place(x=0, y=0)

# NS logo
nsLogo = ImageTk.PhotoImage(Image.open("Images/NS.png"))
nsLogoPanel = Label(window, image=nsLogo)
nsLogoPanel.place(x=50, y=30)

# Top Text
topText = Label(window, text="Laat je ervaring achter en zie jou bericht op een station", bg="#fff")
topText.config(font=('Helvetica bold', 30))
topText.place(x=300, y=50)

# username input
name = Text(window, height=1, width=40)
name.place(x=50, y=200)
name.insert(END, "Vul uw naam in of blijf annoniem")
name.bind("<Button-1>", ClearNameTextField)

# maintext input
mainText = Text(window, height=5, width=40)
mainText.place(x=50, y=240)
mainText.insert(END, "Schrijf uw bericht")
mainText.bind("<Button-1>", ClearMainText_TextField)
mainText.bind("<KeyPress>", OnTextFieldAltered)

# characters used
charactersUsed = Label(window, text="0/140")
charactersUsed.place(x=50, y=330)

# station selection
stationSelection = ttk.Combobox(
    state="readonly",
    values=["Python", "C", "C++", "Java"]
)
stationSelection.place(x=400, y=240)

# Station selection text
topText = Label(window, text="Kies een station", bg="#fff")
topText.config(font=('Helvetica bold', 10))
topText.place(x=401, y=200)

# submit button
submitButton = Button(window, text="       klaar       ", command=SubmitReview)
submitButton.place(x=400, y=330)

DatabaseManager.ConnectToDB()

window.mainloop()

# ---------------------------------------------------------------------------------------------------------------------------
