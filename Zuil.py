from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import WeatherManager
import DatabaseManager

def ReturnPresence(boolean):
    val = "Afwezig"
    if boolean:
        val = "Aanwezig"
    return val


# Triggers when Combobox of selected station is altered
def OpenMessages(index, value, op):
    queryForMessages = "SELECT b.* FROM Bericht b JOIN Beoordelingen bo ON b.BerichtID = bo._BerichtID WHERE b.Station = %s AND bo.IsGoedgekeurd = TRUE ORDER BY b._DateTime DESC LIMIT 5;"
    params = [stationSelection.get()]
    berichten = DatabaseManager.ExecuteSQL_Query(queryForMessages, params, True)

    queryForServices = "SELECT ov_bike, elevator, toilet, park_and_ride FROM StationService WHERE station_city = %s;"
    stationInformation = DatabaseManager.ExecuteSQL_Query(queryForServices, params, True)
    # convert messy list tuple hybrid to just a list
    boolean_list = [item for inner_tuple in stationInformation for item in inner_tuple]

    # Display the services of the station
    services = ["Ov fiets: ", "Lift: ", "WC: ", "Park and ride: "]
    indexer = 4
    infoY = 220
    infoY_increment = 25
    for index in range(indexer):
        label = Label(window, text=services[index] + ReturnPresence(boolean_list[index]), bg="#fff")
        label.config(font=('Helvetica bold', 10))
        label.place(x=500, y=infoY)
        infoY += infoY_increment
        indexer += 1

    calcius = WeatherManager.GetWeatherFromTomorrow(stationSelection.get())
    print(calcius)
    label = Label(window, text="Het weer in " + stationSelection.get() + " is morgen: " + str(WeatherManager.GetWeatherFromTomorrow(stationSelection.get()) + "°"), bg="#fff")
    label.config(font=('Helvetica bold', 10))
    label.place(x=500, y=infoY)

    posX = 150
    posY = 220
    yIncrement = 125
    #Displaying the messages to the "zuil"
    for bericht in berichten:
        name = Label(window, text=bericht[3], bg="#fff")
        name.config(font=('Helvetica bold', 10))
        name.place(x=posX, y=posY)

        mainText = Text(window, height=4, width=40)
        mainText.place(x=posX, y=posY + 20)
        mainText.insert(END, bericht[1])
        mainText.config(state=DISABLED)
        posY += yIncrement


window = Tk()
window.geometry("800x950")
window.resizable(False, False)

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

topText = Label(window, text="Zie hier de laatste reviews van reizers!", bg="#fff")
topText.config(font=('Helvetica bold', 25))
topText.place(x=200, y=50)

# station selection
query = "SELECT station_city FROM StationService;"
station_names = []
station_city_values = tuple(row[0] for row in DatabaseManager.ExecuteSQL_Query(query, False, True))

v = StringVar()
v.trace('w', OpenMessages)
stationSelection = ttk.Combobox(
    state="readonly",
    textvariable=v,
    values=station_city_values
)
stationSelection.place(x=350, y=180)

window.mainloop()
