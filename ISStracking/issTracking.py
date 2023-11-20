

#First we import all the modules/packages we need
import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder 
import subprocess

#Connection with the API to gather the info of the astronauts
url = "http://api.open-notify.org/astros.json"
request = urllib.request.urlopen(url)
response = json.loads(request.read())

#Will open information in a text file
file = open("iss.txt", "w") #create the text file
file.write("There are currently " + str(response["number"]) + " astronauts on the ISS: \n\n" )

people = response['people']#extracting the people from api
for p in people:#for loop to display all people inside
    file.write(p['name'] + " - on board" + "\n")
file.close()
webbrowser.open("iss.txt")

#Setup the world map in turtle module
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

#Load the world map image
screen.bgpic("imageWORLD.gif")
screen.register_shape("imageISS.gif")
iss = turtle.Turtle()
iss.shape("imageISS.gif")
iss.setheading(45)
iss.penup()

#Create a loop that will load the current status of the ISS in real-time
while True: 
    url = "http://api.open-notify.org/iss-now.json"
    request = urllib.request.urlopen(url)
    response = json.loads(request.read())

    #Extract the ISS location
    location = response["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    #Output to the terminal
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\n Longitude: " + str(lon))

    #Update the ISS location
    iss.goto(lon,lat)

    #Refresh each 5 seconds
    time.sleep(5)