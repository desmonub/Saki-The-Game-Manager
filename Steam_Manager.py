import customtkinter as ctk
import tkinter as tk
import cv2
import numpy as np
import pyautogui as pg
import time

class SteamIDManager:
    def __init__(self):
        self.titles = ["Add IDs", "View ID",  "Update ID", "Delete ID", "Login to Steam"]
        self.functions = [self.addst, self.viewst, self.updatest, self.delst, self.loginst]

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
        self.id_no_label = ctk.CTkLabel(self.id_input_frame, text="Steam ID Number:")
        self.id_no_label.pack(side="top", padx=5, pady=5)

        self.id_no_entry = ctk.CTkEntry(self.id_input_frame)
        self.id_no_entry.pack(side="top", padx=5, pady=5)

        # Create the ID username label and input box
        self.id_username_label = ctk.CTkLabel(self.id_input_frame, text="Steam ID Username:")
        self.id_username_label.pack(side="top", padx=5, pady=5)

        self.id_username_entry = ctk.CTkEntry(self.id_input_frame)
        self.id_username_entry.pack(side="top", padx=5, pady=5)

        # Create the ID password label and input box
        self.id_password_label = ctk.CTkLabel(self.id_input_frame, text="Steam ID Password:")
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

    def addst(self):
        # Clear the ID view box
        for widget in self.id_view_box.winfo_children():
            widget.destroy()

        # Get the username and password from the entry widgets
        id_username = self.id_username_entry.get()
        id_password = self.id_password_entry.get()

        # Check if the inputs are not empty
        if id_username and id_password:
            # Open the username and password files for appending
            with open('stusername.txt', 'a') as username_file:
                with open('spass.txt', 'a') as password_file:

                    # Write the username and password to the files
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
        self.id_username_entry.delete(0, tk.END)
        self.id_password_entry.delete(0, tk.END)

    def viewst(self):
        # Clear the ID view box
        for widget in self.id_view_box.winfo_children():
            widget.destroy()

        # Read the username and password files
        with open('stusername.txt', 'r') as username_file:
            username_lines = username_file.readlines()

        with open('spass.txt', 'r') as password_file:
            password_lines = password_file.readlines()

        # Display the usernames and passwords in numerical order
        for i in range(len(username_lines)):
            id_num = i + 1
            id_text = f"ID No. {id_num}"
            username_text = f"Username: {username_lines[i].strip()}"
            password_text = f"Password: {password_lines[i].strip()}\n"

            label = ctk.CTkLabel(self.id_view_box, text=id_text)
            label.pack(pady=5)

            label = ctk.CTkLabel(self.id_view_box, text=username_text)
            label.pack(pady=5)

            label = ctk.CTkLabel(self.id_view_box, text=password_text)
            label.pack(pady=5)

    def updatest(self):
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

        username_path = 'stusername.txt'
        password_path = 'spass.txt'

        with open(username_path, 'r') as username_file, open(password_path,'r') as password_file:
            username_lines = username_file.readlines()
            password_lines = password_file.readlines()

        if 0 <= serial_number < len(username_lines):
            # Get the new username and password from the entry widgets
            new_username = self.id_username_entry.get()
            new_password = self.id_password_entry.get()

            username_lines[serial_number] = new_username + '\n'
            password_lines[serial_number] = new_password + '\n'

            with open(username_path, 'w') as username_file, open(password_path,'w') as password_file:
                username_file.writelines(username_lines)
                password_file.writelines(password_lines)

            # Display a confirmation message in the viewbox
            confirmation_label = ctk.CTkLabel(self.id_view_box, text="Your Steam ID is successfully updated.")
            confirmation_label.pack(side="top", padx=5, pady=5)
        else:
            # Display an error message in the viewbox
            error_label = ctk.CTkLabel(self.id_view_box, text=f"Serial number {serial_number+1} is out of range.")
            error_label.pack(side="top", padx=5, pady=5)

        # Clear the entry widgets
        self.id_no_entry.delete(0, tk.END)
        self.id_username_entry.delete(0, tk.END)
        self.id_password_entry.delete(0, tk.END)

    def delst(self):
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

        username_path = 'stusername.txt'
        password_path = 'spass.txt'

        with open(username_path, 'r') as username_file, open(password_path,'r') as password_file:
            username_lines = username_file.readlines()
            password_lines = password_file.readlines()

        if 0 <= serial_number < len(username_lines):
            # Delete the specified entries
            del username_lines[serial_number]
            del password_lines[serial_number]

            with open(username_path, 'w') as username_file, open(password_path,'w') as password_file:
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
        self.id_username_entry.delete(0, tk.END)
        self.id_password_entry.delete(0, tk.END)

    def loginst(self):
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

        username_path = 'stusername.txt'
        password_path = 'spass.txt'

        with open(username_path, 'r') as username_file, open(password_path,'r') as password_file:
            username_lines = username_file.readlines()
            password_lines = password_file.readlines()

        if 0 <= serial_number < len(username_lines):
            # Get the username and password for the given ID number
            x = username_lines[serial_number].strip()
            y = password_lines[serial_number].strip()

            threshold = 0.8
            time.sleep(1)
            pg.press("win")
            time.sleep(1)
            pg.write("steam")
            pg.press("enter")
            splus_image = cv2.imread('ima/splus.png', cv2.IMREAD_COLOR)
            SUN_image = cv2.imread('ima/sun.png', cv2.IMREAD_COLOR)
            SPW_image = cv2.imread('ima/spw.png', cv2.IMREAD_COLOR)
            SLP_image = cv2.imread('ima/slp.png', cv2.IMREAD_COLOR)
            while True:
                screen_pil = pg.screenshot()
                screen_np = np.array(screen_pil)
                screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

                spresult = cv2.matchTemplate(screen, splus_image, cv2.TM_CCOEFF_NORMED)
                spmin_val, spmax_val, spmin_loc, spmax_loc = cv2.minMaxLoc(spresult)
                threshold = 0.8
                if spmax_val >= threshold:
                    un_x, un_y = spmax_loc
                    pg.moveTo(un_x+10,un_y+10,0.00000000000001)
                    pg.click(button='left')
                    cv2.destroyAllWindows()
                    time.sleep(0.5)
                    screen_pil = pg.screenshot()
                    screen_np = np.array(screen_pil)
                    screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
                    time.sleep(0.5)
                    sunresult = cv2.matchTemplate(screen, SUN_image, cv2.TM_CCOEFF_NORMED)
                    sunmin_val, sunmax_val, sunmin_loc, sunmax_loc = cv2.minMaxLoc(sunresult)
                    spwresult = cv2.matchTemplate(screen, SPW_image, cv2.TM_CCOEFF_NORMED)
                    spwin_val, spwmax_val, spwmin_loc, spwmax_loc = cv2.minMaxLoc(spwresult)
                    if sunmax_val >= threshold:
                        sun_x, sun_y = sunmax_loc
                        spw_x, spw_y = spwmax_loc
                        pg.moveTo(sun_x+35,sun_y+35,0.00000000000001)
                        pg.click(button='left')
                        pg.write(x)
                        pg.moveTo(spw_x+35,spw_y+35,0.00000000000001)
                        pg.click(button='left')
                        pg.write(y)
                        break
                    cv2.destroyAllWindows()
        else:
            # Display an error message in the viewbox
            error_label = ctk.CTkLabel(self.id_view_box, text=f"Serial number {serial_number+1} is out of range.")
            error_label.pack(side="top", padx=5, pady=5)

        # Clear the entry widgets
        self.id_no_entry.delete(0, tk.END)
        self.id_username_entry.delete(0, tk.END)
        self.id_password_entry.delete(0, tk.END)
pass

def run():
    app = SteamIDManager()
    app.root.mainloop()

if __name__ == "__main__":
    run()
