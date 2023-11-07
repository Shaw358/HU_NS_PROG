from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
# FIXME: Importing the main file into UserWindow one seems like a bad idea... Too bad!
import csv
from datetime import datetime
import datetime
import DatabaseManager


# Helper functions
def DateGrabber():
    return datetime.datetime.today().replace(microsecond=0)


def Submit():
    indexer = 0
    for val in choices:
        if val == "Toelaten":
            val = True
        else:
            val = False
        query = "INSERT INTO Beoordelingen (_DateTime, ModeratorNaam, ModeratorEmail, _BerichtID, IsGoedgekeurd) VALUES (%s, %s, %s, %s, %s);"
        params = (DateGrabber(), name.get("1.0", 'end-1c'), email.get("1.0", 'end-1c'), IDsOfMessages[indexer], val)
        DatabaseManager.ExecuteSQL_Query(query, params, False)
        indexer += 1


def OpenMessages():
    query = f"SELECT * FROM Bericht;"
    rows = DatabaseManager.ExecuteSQL_Query(query, False, True)

    skipFirst = True
    posX = 50
    posY = 170

    yIncrement = 100
    # 0 = ID, 1 = Message, 2 = DateTime, 3 = Name, 4 = Station
    for row in rows:
        if True:
            print(row[0])
            IDsOfMessages.append(row[0])
            username = Label(window, text=str(row[3]))
            username.place(x=posX, y=posY)

            mainText = Text(window, height=4, width=40)
            mainText.place(x=posX, y=posY + 20)
            mainText.insert(END, row[1])
            mainText.config(state=DISABLED)

            stationSelection = ttk.Combobox(
                state="readonly",
                values=["Toelaten", "Weigeren"]
            )
            stationSelection.place(x=posX + 180, y=posY)
            choices.append(stationSelection)

            posY += yIncrement


window = Tk()
window.geometry("1400x900")
window.resizable(False, False)

# Yellow Top Bar
topBarBg = ImageTk.PhotoImage(Image.open("Images/YB.png"))
topBarBgPanel = Label(window, image=topBarBg)
topBarBgPanel.place(x=0, y=0)

# NS logo
nsLogo = ImageTk.PhotoImage(Image.open("Images/NS.png"))
nsLogoPanel = Label(window, image=nsLogo)
nsLogoPanel.place(x=50, y=30)

topText = Label(window, text="Moderatie team NS", bg="#fff")
topText.config(font=('Helvetica bold', 30))
topText.place(x=300, y=50)

# submit button
submitButton = Button(window, text="       klaar       ", command=Submit)
submitButton.place(x=400, y=200)

name = Text(window, height=1, width=40)
name.place(x=600, y=300)
name.insert(END, "Naam")

email = Text(window, height=1, width=40)
email.place(x=600, y=400)
email.insert(END, "Email")

choices = []
IDsOfMessages = []

OpenMessages()

window.mainloop()
