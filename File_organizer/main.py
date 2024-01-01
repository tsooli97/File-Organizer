import tkinter as tk
from tkinter import Canvas, IntVar
from PIL import Image, ImageTk
import os
from logic import select_directory, organize_files, undo_organization, open_explorer, organize

# Global list to track the movements of files during the organization process
file_movements = []


def main():
    """
    Main function to set up and run the Tkinter GUI for the file organizer application.
    """
    window = tk.Tk()
    window.minsize(450, 450)
    window.resizable(False, False)
    window.config(padx=50, pady=50)
    window.title("File Organizer")

    # Set up the canvas to display an image
    canvas = Canvas(width=400, height=400)
    image = Image.open("logo.jpg")
    image = image.resize((400, 400))
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(200, 200, image=photo)
    canvas.grid(column=0, row=0, columnspan=2)

    # Initialize Tkinter variables and widgets
    global directory_label, status_label, open_after_organize, undo_label
    open_after_organize = IntVar()

    # Button to select a directory
    select_button = tk.Button(window, text="Select Directory", command=lambda: select_directory(directory_label))
    select_button.grid(column=0, row=1, sticky="w", pady=10)

    # Checkbutton to choose whether to open the directory after organizing
    open_toggle = tk.Checkbutton(window, text="Open directory after organizing", variable=open_after_organize)
    open_toggle.grid(column=0, row=3, sticky="w")

    # Label to display the selected directory
    directory_label = tk.Label(window, text="", fg="blue")
    directory_label.grid(column=1, row=1)

    # Button to start the file organization process
    organize_button = tk.Button(window, text="Organize Files", command=lambda: organize_files(directory_label,
                                status_label, file_movements, open_after_organize, organize, window))

    organize_button.grid(column=0, row=2, sticky="w", pady=5)

    # Button to undo the last organization action
    undo_button = tk.Button(window, text="Undo Organization", command=lambda: undo_organization(directory_label,
                            status_label, file_movements, window))
    undo_button.grid(column=0, row=4, sticky="w", pady=5)

    # Label to display status messages
    status_label = tk.Label(window, text="", fg="red")
    status_label.grid(column=1, row=3)

    # Start the Tkinter event loop
    window.mainloop()


if __name__ == "__main__":
    main()
