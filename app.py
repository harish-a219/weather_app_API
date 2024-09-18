import requests 
import tkinter as tk
from PIL import Image, ImageTk

def getImage ():
   global image_label
   global img
   Sun = Image.open(f"{icon}.png")
   print(icon)
   resize_image = Sun.resize((600, 600))
   img = ImageTk.PhotoImage(resize_image)
   image_label = tk.Label(weather_app, image = img)
   image_label.pack(side= "bottom", fill= "both", expand= "yes") #Pack gets the label to display on the screen
   print(img)

#Global - Your variable can be accessed anywhere in your code 

icon = "01d"
def weatherMeasure ():
 #Someone enters city name 
  global icon

  city = city_entry.get()
  weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID=d872258c216b817fb79e5d07d9934231")
  if weather_data.json()["cod"] == "404":
    result_label.config(text = "Error! Please enter a proper city")
  else:
    #Creates a result label (like a print statment.) and inside parentheses, we want to display "text," which is the answer to the variable city
    result_label.config(text = "The weather in " + city + " is" + "  " + str(weather_data.json()["main"]["temp"]) + " " + "° F" + " " + str(weather_data.json()["weather"][0]["main"]) + " ")
    icon = weather_data.json()["weather"][0]["icon"]
    getImage()
  
#"tk" is a package with a function called "Tk" which is used to create a screen/app.
weather_app = tk.Tk()
weather_app.title("Weather")
tk.Label(weather_app, text = "Enter a city: ")

Sun = Image.open(f"01d.png")
resize_image = Sun.resize((600, 600))
img = ImageTk.PhotoImage(resize_image)
image_label = tk.Label(weather_app, image = img)
#Ready to submit city, "pack" gets the component ready to display
tk.Button(weather_app, text = "Submit City", command = weatherMeasure).pack()

#Label is something you are displaying. We can't display just the Sun, so we display it in a Label (just how we do "text =")
#We are resizing the image to make it appear bigger on the screen by setting the width and height (pixels) to a value of our choice
#We then are telling the computer when it opens the image in the computer, to make it in our pixel w/h (line 53)

city_entry = tk.Entry(weather_app, text = "Enter a city: ")
city_entry.pack()
result_label = tk.Label(weather_app, text = "The weather is")
result_label.pack()
#Starts the app - mainloop
image_label.pack_forget() #pack_forget loads it onto screen, but hides it. Used in the start of the program to hide the sun.
weather_app.mainloop()


#Tkinter documentation search in google
#get request - gets info from a different computer
#post request - posts info 
#.json changes response to different language - more user friendly


   