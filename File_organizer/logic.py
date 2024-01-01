import os
import shutil
import subprocess
from tkinter import filedialog


def organize(directory, file_movements):
    """
    Organizes files in the given directory into subfolders based on their file types.

    Parameters:
    directory (str): The directory whose files are to be organized.
    file_movements (list): A list to record the movements of files for undo functionality.

    The function currently supports organizing .txt, .pdf, .docx, .xlsx, .jpg, .png, .mp3 and .mp4 files.
    """
    
    directory_location = os.listdir(directory)

    for item in directory_location:
        original_path = os.path.join(directory, item)
        target_directory = None

        if item.endswith(".txt"):
            target_directory = os.path.join(directory, "Text Files")
        elif item.endswith(".pdf"):
            target_directory = os.path.join(directory, "PDF Files")
        elif item.endswith(".docx"):
            target_directory = os.path.join(directory, "Word Documents")
        elif item.endswith(".xlsx"):
            target_directory = os.path.join(directory, "Excel Spreadsheets")
        elif item.endswith(".jpg") or item.endswith(".png"):
            target_directory = os.path.join(directory, "Images")
        elif item.endswith(".mp3"):
            target_directory = os.path.join(directory, "Audio Files")
        elif item.endswith(".mp4"):
            target_directory = os.path.join(directory, "Video Files")

        if target_directory:
            try:
                if not os.path.exists(target_directory):
                    os.mkdir(target_directory)
                new_path = os.path.join(target_directory, item)
                shutil.move(original_path, new_path)
                file_movements.append((original_path, new_path))
            except OSError as e:
                print(f"Error organizing file {item}: {e}")


def select_directory(directory_label):
    """
    Opens a dialog for the user to select a directory and updates the directory_label with the chosen path.

    Parameters:
    directory_label (tk.Label): The label widget to display the selected directory.
    """

    directory = filedialog.askdirectory()
    if directory:
        directory_label.config(text=directory)
    return directory


def organize_files(directory_label, status_label, file_movements, open_after_organize, organize_function, window):
    """
    Organizes files in the selected directory and updates the status label. Optionally opens the directory in Explorer.

    Parameters:
    directory_label (tk.Label): Label showing the selected directory.
    status_label (tk.Label): Label to display the status message.
    file_movements (list): List to track file movements.
    open_after_organize (tk.IntVar): Variable to check if the directory should be opened after organization.
    organize_function (function): Function to organize files in the directory.
    open_explorer_function (function): Function to open the directory in Explorer.
    window (tk.Tk): The main application window.
    """

    directory = directory_label.cget("text")
    if directory:
        try:
            current_movements = []
            organize_function(directory, current_movements)
            if current_movements:
                file_movements.append(current_movements)
            status_label.config(text="Files organized successfully!",fg="green")
        except Exception as e:
            status_label.config(text=f"Error: {e}", fg="red")
        finally:
            window.after(3000, lambda: clear_status_label(status_label))

        if open_after_organize.get() == 1:
            open_explorer(directory)
    else:
        status_label.config(text="Please select a directory first.", fg="red")
        window.after(3000, lambda: clear_status_label(status_label))


def undo_organization(directory_label, status_label, file_movements, window):
    """
    Reverts the organization of files by moving them back to their original locations.

    Parameters:
    directory_label (tk.Label): Label showing the selected directory.
    status_label (tk.Label): Label to display the status message.
    file_movements (list): List to track file movements.
    window (tk.Tk): The main application window.
    """

    directory = directory_label.cget("text")
    if directory:
        if file_movements:
            last_movements = file_movements.pop()
            for original_path, new_path in reversed(last_movements):
                shutil.move(new_path, original_path)
            status_label.config(text="Undo complete!", fg="green")
            window.after(3000, lambda: clear_status_label(status_label))
        else:
            status_label.config(text="No organization actions to undo.", fg="red")
            window.after(3000, lambda: clear_status_label(status_label))
    else:
        status_label.config(text="Please select a directory first.", fg="red")
        window.after(3000, lambda: clear_status_label(status_label))


def open_explorer(path):
    """
    Opens the specified path in Windows Explorer.

    Parameters:
    path (str): The path to be opened in Windows Explorer.
    """

    normalized_path = os.path.normpath(path)
    subprocess.Popen(f'explorer "{normalized_path}"')


def clear_status_label(status_label):
    """
    Clears the text of the given status label.

    Parameters:
    status_label (tk.Label): The label to be cleared.
    """

    status_label.config(text="")
