import customtkinter as ctk
import tkinter as tk
import cv2
import numpy as np
import pyautogui as pg
import time

class ValorantIDManager:
    def __init__(self):
        self.titles = ["Add IDs", "View ID",  "Update ID", "Delete ID", "Login to Valorant"]
        self.functions = [self.addvaloid, self.viewvaloid, self.editvaloid, self.deletevaloid, self.login]

        # Create the main window
        self.root = ctk.CTk()
        self.root.iconbitmap('ima/logo.ico')
        window_width = 850
        window_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the geometry of the window to center it
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.root.title("ID Management")

        # Set the minimum and maximum size of the window
        self.root.minsize(850, 400)  # Minimum size (width, height)
        self.root.maxsize(1050, 450)  # Maximum size (width, height)

        # Create the ID input frame
        self.id_input_frame = ctk.CTkFrame(self.root)
        self.id_input_frame.pack(side="left", padx=20, pady=20)

        # Create the ID number label and input box
        self.id_no_label = ctk.CTkLabel(self.id_input_frame, text="ID Number:")
        self.id_no_label.pack(side="top", padx=5, pady=5)

        self.id_no_entry = ctk.CTkEntry(self.id_input_frame)
        self.id_no_entry.pack(side="top", padx=5, pady=5)

        # Create the ID name label and input box
        self.id_name_label = ctk.CTkLabel(self.id_input_frame, text="ID Name:")
        self.id_name_label.pack(side="top", padx=5, pady=5)

        self.id_name_entry = ctk.CTkEntry(self.id_input_frame)
        self.id_name_entry.pack(side="top", padx=5, pady=5)

        # Create the ID username label and input box
        self.id_username_label = ctk.CTkLabel(self.id_input_frame, text="ID Username:")
        self.id_username_label.pack(side="top", padx=5, pady=5)

        self.id_username_entry = ctk.CTkEntry(self.id_input_frame)
        self.id_username_entry.pack(side="top", padx=5, pady=5)

        # Create the ID password label and input box
        self.id_password_label = ctk.CTkLabel(self.id_input_frame, text="ID Password:")
        self.id_password_label.pack(side="top", padx=5, pady=5)

        self.id_password_entry = ctk.CTkEntry(self.id_input_frame)
        self.id_password_entry.pack(side="top", padx=5, pady=5)

        # Create the ID view box
        self.id_view_box = ctk.CTkScrollableFrame(self.root, width=400, height=300, border_width=1, corner_radius=10)
        self.id_view_box.pack(side="left", padx=20, pady=20)

        # Create the buttons frame
        self.buttons_frame = ctk.CTkFrame(self.root)
        self.buttons_frame.pack(side="right", padx=20, pady=20)

        # Create buttons for each function
        for i in range(len(self.titles)):
            button = ctk.CTkButton(self.buttons_frame, text=self.titles[i], command=self.functions[i])
            button.grid(row=i, column=0, pady=10)

    def viewvaloid(self):
            # Clear the ID view box
            for widget in self.id_view_box.winfo_children():
                widget.destroy()

            # Read the ID, username, and password files
            with open('id.txt', 'r') as id_file:
                id_lines = id_file.readlines()

            with open('username.txt', 'r') as username_file:
                username_lines = username_file.readlines()

            with open('pass.txt', 'r') as password_file:
                password_lines = password_file.readlines()

            # Display the IDs, usernames, and passwords in numerical order
            for i in range(len(id_lines)):
                id_num = i + 1
                id_text = f"ID No. {id_num}: {id_lines[i].strip()}"
                username_text = f"Username: {username_lines[i].strip()}"
                password_text = f"Password: {password_lines[i].strip()}\n"

                label = ctk.CTkLabel(self.id_view_box, text=id_text)
                label.pack(pady=5)

                label = ctk.CTkLabel(self.id_view_box, text=username_text)
                label.pack(pady=5)

                label = ctk.CTkLabel(self.id_view_box, text=password_text)
                label.pack(pady=5)

    def addvaloid(self):
        # Clear the ID view box
        for widget in self.id_view_box.winfo_children():
            widget.destroy()

        # Get the ID information from the entry widgets
        id_name = self.id_name_entry.get()
        id_username = self.id_username_entry.get()
        id_password = self.id_password_entry.get()

        # Check if the inputs are not empty
        if id_name and id_username and id_password:
            # Open the ID, username, and password files for appending
            with open('id.txt', 'a') as id_file:
                with open('username.txt', 'a') as username_file:
                    with open('pass.txt', 'a') as password_file:

                        # Write the ID information to the files
                        id_file.write(id_name + '\n')
                        username_file.write(id_username + '\n')
                        password_file.write(id_password + '\n')

            # Display a confirmation message in the viewbox
            confirmation_label = ctk.CTkLabel(self.id_view_box, text="Your ID is successfully being added.")
            confirmation_label.pack(side="top", padx=5, pady=5)
        else:
            # Display an error message in the viewbox
            error_label = ctk.CTkLabel(self.id_view_box, text="Error: All fields must be filled.")
            error_label.pack(side="top", padx=5, pady=5)

        # Clear the entry widgets
        self.id_name_entry.delete(0, tk.END)
        self.id_username_entry.delete(0, tk.END)
        self.id_password_entry.delete(0, tk.END)

    def editvaloid(self):
            # Clear the ID view box
        for widget in self.id_view_box.winfo_children():
            widget.destroy()

        # Get the serial number from the ID number entry widget
        serial_number_str = self.id_no_entry.get()

        # Check if the serial number string is not empty
        if not serial_number_str:
            error_label = ctk.CTkLabel(self.id_view_box, text="Error: ID Number field must not be empty.")
            error_label.pack(side="top", padx=5, pady=5)
            return

        serial_number = int(serial_number_str)
        serial_number = serial_number - 1

        id_path = 'id.txt'
        username_path = 'username.txt'
        password_path = 'pass.txt'

        with open(id_path, 'r') as id_file, open(username_path, 'r') as username_file, open(password_path,'r') as password_file:
            id_lines = id_file.readlines()
            username_lines = username_file.readlines()
            password_lines = password_file.readlines()

        if 0 <= serial_number < len(id_lines):
            # Get the new ID, username, and password from the entry widgets
            new_id = self.id_name_entry.get()
            new_username = self.id_username_entry.get()
            new_password = self.id_password_entry.get()

            id_lines[serial_number] = new_id + '\n'
            username_lines[serial_number] = new_username + '\n'
            password_lines[serial_number] = new_password + '\n'

            with open(id_path, 'w') as id_file, open(username_path, 'w') as username_file, open(password_path,'w') as password_file:
                id_file.writelines(id_lines)
                username_file.writelines(username_lines)
                password_file.writelines(password_lines)

            # Display a confirmation message in the viewbox
            confirmation_label = ctk.CTkLabel(self.id_view_box, text="Your Valorant ID is successfully updated.")
            confirmation_label.pack(side="top", padx=5, pady=5)
        else:
            # Display an error message in the viewbox
            error_label = ctk.CTkLabel(self.id_view_box, text=f"Serial number {serial_number+1} is out of range.")
            error_label.pack(side="top", padx=5, pady=5)

        # Clear the entry widgets
        self.id_no_entry.delete(0, tk.END)
        self.id_name_entry.delete(0, tk.END)
        self.id_username_entry.delete(0, tk.END)
        self.id_password_entry.delete(0, tk.END)

    def deletevaloid(self):
        # Clear the ID view box
        for widget in self.id_view_box.winfo_children():
            widget.destroy()

        # Get the serial number from the ID number entry widget
        serial_number_str = self.id_no_entry.get()

        # Check if the serial number string is not empty
        if not serial_number_str:
            error_label = ctk.CTkLabel(self.id_view_box, text="Error: ID Number field must not be empty.")
            error_label.pack(side="top", padx=5, pady=5)
            return

        serial_number = int(serial_number_str)
        serial_number = serial_number - 1

        id_path = 'id.txt'
        username_path = 'username.txt'
        password_path = 'pass.txt'

        with open(id_path, 'r') as id_file, open(username_path, 'r') as username_file, open(password_path,'r') as password_file:
            id_lines = id_file.readlines()
            username_lines = username_file.readlines()
            password_lines = password_file.readlines()

        if 0 <= serial_number < len(id_lines):
            # Delete the specified entries
            del id_lines[serial_number]
            del username_lines[serial_number]
            del password_lines[serial_number]

            with open(id_path, 'w') as id_file, open(username_path, 'w') as username_file, open(password_path,'w') as password_file:
                id_file.writelines(id_lines)
                username_file.writelines(username_lines)
                password_file.writelines(password_lines)

            # Display a confirmation message in the viewbox
            confirmation_label = ctk.CTkLabel(self.id_view_box, text=f"Entry with serial number {serial_number+1} has been deleted.")
            confirmation_label.pack(side="top", padx=5, pady=5)
        else:
            # Display an error message in the viewbox
            error_label = ctk.CTkLabel(self.id_view_box, text=f"Serial number {serial_number+1} is out of range.")
            error_label.pack(side="top", padx=5, pady=5)

        # Clear the entry widgets
        self.id_no_entry.delete(0, tk.END)
        self.id_name_entry.delete(0, tk.END)
        self.id_username_entry.delete(0, tk.END)
        self.id_password_entry.delete(0, tk.END)

    def login(self):
            # Get the serial number from the ID number entry widget
            serial_number_str = self.id_no_entry.get()

            # Check if the serial number string is not empty
            if not serial_number_str:
                error_label = ctk.CTkLabel(self.id_view_box, text="Error: ID Number field must not be empty.")
                error_label.pack(side="top", padx=5, pady=5)
                return

            serial_number = int(serial_number_str)
            serial_number = serial_number - 1

            id_path = 'id.txt'
            username_path = 'username.txt'
            password_path = 'pass.txt'

            with open(id_path, 'r') as id_file, open(username_path, 'r') as username_file, open(password_path,'r') as password_file:
                id_lines = id_file.readlines()
                username_lines = username_file.readlines()
                password_lines = password_file.readlines()

            if 0 <= serial_number < len(id_lines):
                x = username_lines[serial_number].strip()
                y = password_lines[serial_number].strip()

                time.sleep(1)
                pg.press("win")
                time.sleep(1)
                pg.write("valorant")
                pg.press("enter")
                UN_image_path = r'ima\un.png'
                PW_image_path = r'ima\pw.png'

                UN_image = cv2.imread(UN_image_path, cv2.IMREAD_COLOR)
                PW_image = cv2.imread(PW_image_path, cv2.IMREAD_COLOR)

                while True:
                    screen_pil = pg.screenshot()
                    screen_np = np.array(screen_pil)
                    screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

                    result = cv2.matchTemplate(screen, UN_image, cv2.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

                    result2 = cv2.matchTemplate(screen, PW_image, cv2.TM_CCOEFF_NORMED)
                    min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)

                    threshold = 0.8
                    if max_val >= threshold:
                        un_x, un_y = max_loc
                        pw_x, pw_y = max_loc2

                        pg.moveTo(un_x + 41, un_y + 32, 0.00000000000001)
                        pg.click(button='left')
                        pg.write(x)
                        pg.moveTo(pw_x + 41, pw_y + 32, 0.00000000000001)
                        pg.click(button='left')
                        pg.write(y)
                        pg.press("enter")
                        break
                cv2.destroyAllWindows()
            else:
                # Display an error message in the viewbox
                error_label = ctk.CTkLabel(self.id_view_box, text=f"Serial number {serial_number+1} is out of range.")
                error_label.pack(side="top", padx=5, pady=5)

            # Clear the entry widgets
            self.id_no_entry.delete(0, tk.END)
            self.id_name_entry.delete(0, tk.END)
            self.id_username_entry.delete(0, tk.END)
            self.id_password_entry.delete(0, tk.END)
pass

def run():
    app = ValorantIDManager()
    app.root.mainloop()

if __name__ == "__main__":
    run()