# This is the GUI of the application
# Maison Kasprick - 11/4/2024
# Version 1.0

# Imports
import tkinter
import customtkinter

# System Settings
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('dark-blue')

# GUI frame
app = customtkinter.CTk()
app.geometry('720x480')
app.title('YouTube Downloader')

# UI Elements
title = customtkinter.CTkLabel(app, text = 'Insert a YouTube link')
title.pack(padx = 10, pady = 10)

# Link input
input_link = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 40, textvariable = input_link)
link.pack()

# Finished Downloading
finish_label = customtkinter.CTkLabel(app, text = '')
finish_label.pack()

# Download buttons
button_mp3 = customtkinter.CTkButton(app, text = 'Download MP3')
button_mp3.pack(padx = 10, pady = 10)
button_mp4 = customtkinter.CTkButton(app, text = 'Download MP4')
button_mp4.pack(padx = 10, pady = 10)

# Run GUI
app.mainloop()
