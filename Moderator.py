from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
# FIXME: Importing the main file into UserWindow one seems like a bad idea... Too bad!
import csv
from datetime import datetime
import datetime


# Helper functions
def DateGrabber():
    return datetime.date.today()


def TimeStampGrabber():
    return datetime.datetime.now().time()


def Submit():
    data = ["Date", "Timestamp", "User", "Message", "Station", "ModerationResult", "ModerationDate", "ModerationTime",
            "ModeratorName", "ModeratorEmail"]

    with open('messagesModerated.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file)

        with open('messages.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            indexer = -1
            for row in reader:
                if indexer >= 0:
                    row += [choices[indexer].get(), DateGrabber(), TimeStampGrabber(), name.get('1.0', 'end-1c'), email.get('1.0', 'end-1c')]
                    csv_writer.writerow(row)
                indexer += 1


def OpenMessages():
    db = open('messages.csv', 'r')
    csv_reader = csv.reader(db)

    indexer = 0
    posX = 50
    posY = 170

    yIncrement = 100
    # NOTE: 0 = date, 1 = timestamp, 2 = user, 3 = message, 4 = station
    for row in csv_reader:
        username = Label(window, text=str(row[2]))
        username.place(x=posX, y=posY)

        mainText = Text(window, height=4, width=40)
        mainText.place(x=posX, y=posY + 20)
        mainText.insert(END, row[3])
        mainText.config(state=DISABLED)

        stationSelection = ttk.Combobox(
            state="readonly",
            values=["Toelaten", "Weigeren"]
        )
        stationSelection.place(x=posX + 180, y=posY)
        choices.append(stationSelection)

        indexer += 1
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

OpenMessages()

window.mainloop()
