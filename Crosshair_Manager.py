import customtkinter as ctk
import tkinter as tk
import cv2
import numpy as np
import pyautogui as pg
import time

class CrosshairManager:
    def __init__(self):
        self.titles = ["Add Crosshair", "View Crosshairs", "Delete Crosshair", "Input Crosshair"]
        self.functions = [self.crossadd, self.crossview, self.crossdele, self.input]

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
        self.root.title("Crosshair Management")

        # Set the minimum and maximum size of the window
        self.root.minsize(850, 400)  # Minimum size (width, height)
        self.root.maxsize(1050, 450)  # Maximum size (width, height)

        # Create the Crosshair input frame
        self.cross_input_frame = ctk.CTkFrame(self.root)
        self.cross_input_frame.pack(side="left", padx=20, pady=20)

        # Create the Crosshair number label and input box
        self.crosshair_no_label = ctk.CTkLabel(self.cross_input_frame, text="Crosshair Number:")
        self.crosshair_no_label.pack(side="top", padx=5, pady=5)

        self.crosshair_no_entry = ctk.CTkEntry(self.cross_input_frame)
        self.crosshair_no_entry.pack(side="top", padx=5, pady=5)

        # Create the Crosshair name label and input box
        self.crosshair_name_label = ctk.CTkLabel(self.cross_input_frame, text="Crosshair Name:")
        self.crosshair_name_label.pack(side="top", padx=5, pady=5)

        self.crosshair_name_entry = ctk.CTkEntry(self.cross_input_frame)
        self.crosshair_name_entry.pack(side="top", padx=5, pady=5)

        # Create the Crosshair code label and input box
        self.crosshair_code_label = ctk.CTkLabel(self.cross_input_frame, text="Crosshair Code:")
        self.crosshair_code_label.pack(side="top", padx=5, pady=5)

        self.crosshair_code_entry = ctk.CTkEntry(self.cross_input_frame)
        self.crosshair_code_entry.pack(side="top", padx=5, pady=5)

        # Create the Crosshair view box
        self.cross_view_box = ctk.CTkScrollableFrame(self.root, width=400, height=300, border_width=1, corner_radius=10)
        self.cross_view_box.pack(side="left", padx=20, pady=20)

        # Create the buttons frame
        self.buttons_frame = ctk.CTkFrame(self.root)
        self.buttons_frame.pack(side="right", padx=20, pady=20)

        # Create buttons for each function
        for i in range(len(self.titles)):
            button = ctk.CTkButton(self.buttons_frame, text=self.titles[i], command=self.functions[i])
            button.grid(row=i, column=0, pady=10)

    def crossadd(self):
        # Clear the Crosshair view box
        for widget in self.cross_view_box.winfo_children():
            widget.destroy()

        # Get the Crosshair information from the entry widgets
        crosshair_name = self.crosshair_name_entry.get()
        crosshair_code = self.crosshair_code_entry.get()

        # Check if the inputs are not empty
        if crosshair_name and crosshair_code:
            # Open the Crosshair name and code files for appending
            with open('crossname.txt', 'a') as chn_file, open('crosscode.txt', 'a') as ch_file:
                # Write the Crosshair information to the files
                chn_file.write(crosshair_name + '\n')
                ch_file.write(crosshair_code + '\n')

            # Display a confirmation message in the viewbox
            confirmation_label = ctk.CTkLabel(self.cross_view_box, text="Crosshair added successfully.")
            confirmation_label.pack(side="top", padx=5, pady=5)
        else:
            # Display an error message in the viewbox
            error_label = ctk.CTkLabel(self.cross_view_box, text="Error: All fields must be filled.")
            error_label.pack(side="top", padx=5, pady=5)

        # Clear the entry widgets
        self.crosshair_no_entry.delete(0, tk.END)
        self.crosshair_name_entry.delete(0, tk.END)
        self.crosshair_code_entry.delete(0, tk.END)

    def crossview(self):
        # Clear the Crosshair view box
        for widget in self.cross_view_box.winfo_children():
            widget.destroy()

        chn_path = 'crossname.txt'
        ch_path = 'crosscode.txt'

        with open(chn_path, 'r') as chn_file, open(ch_path, 'r') as ch_file:
            chn_lines = chn_file.readlines()
            ch_lines = ch_file.readlines()

        for i in range(len(chn_lines)):
            crosshair_name = chn_lines[i].strip()
            crosshair_label = ctk.CTkLabel(self.cross_view_box, text=f"S.no -> {i+1}\nCrosshair -> {crosshair_name}")
            crosshair_label.pack(side="top", padx=5, pady=5)

    def crossdele(self):
        # Clear the Crosshair view box
        for widget in self.cross_view_box.winfo_children():
            widget.destroy()

        # Get the serial number from the ID number entry widget
        serial_number_str = self.crosshair_no_entry.get()

        # Check if the serial number string is not empty
        if not serial_number_str:
            error_label = ctk.CTkLabel(self.cross_view_box, text="Error: ID Number field must not be empty.")
            error_label.pack(side="top", padx=5, pady=5)
            return

        serial_number = int(serial_number_str)
        serial_number = serial_number - 1

        chn_path = 'crossname.txt'
        ch_path = 'crosscode.txt'

        with open(chn_path, 'r') as chn_file, open(ch_path, 'r') as ch_file:
            chn_lines = chn_file.readlines()
            ch_lines = ch_file.readlines()

        if 0 <= serial_number < len(chn_lines):
            del chn_lines[serial_number]
            del ch_lines[serial_number]

            with open(chn_path, 'w') as chn_file, open(ch_path, 'w') as ch_file:
                chn_file.writelines(chn_lines)
                ch_file.writelines(ch_lines)

            # Display a confirmation message in the viewbox
            confirmation_label = ctk.CTkLabel(self.cross_view_box, text=f"Entry with serial number {serial_number+1} has been deleted.")
            confirmation_label.pack(side="top", padx=5, pady=5)
        else:
            # Display an error message in the viewbox
            error_label = ctk.CTkLabel(self.cross_view_box, text=f"Serial number {serial_number+1} is out of range.")
            error_label.pack(side="top", padx=5, pady=5)

        # Clear the entry widgets
        self.crosshair_no_entry.delete(0, tk.END)
        self.crosshair_name_entry.delete(0, tk.END)
        self.crosshair_code_entry.delete(0, tk.END)

    def input(self):
        for widget in self.cross_view_box.winfo_children():
            widget.destroy()
        text_label = ctk.CTkLabel(self.cross_view_box,text=f"!!!!!!!! Works only in home screen of valorant !!!!!!!!")
        text_label.pack(side="top", padx=5, pady=5)
        chn = open('crosscode.txt', 'r')
        text_label = ctk.CTkLabel(self.cross_view_box, text=f"Enter the s.no of crosshair ")
        text_label.pack(side="top", padx=5, pady=5)
        chno_str = self.crosshair_no_entry.get()
        l = 1
        if not chno_str:
            error_label = ctk.CTkLabel(self.cross_view_box, text="Error: ID Number field must not be empty.")
            error_label.pack(side="top", padx=5, pady=5)
            return

        chno = int(chno_str)
        while l <= chno:
            c = chn.readline()
            l = l + 1
        sett_image = cv2.imread('ima/sett.png', cv2.IMREAD_COLOR)
        setl_image = cv2.imread('ima/setl.png', cv2.IMREAD_COLOR)
        croha_image = cv2.imread('ima/croha.png', cv2.IMREAD_COLOR)
        impo_image = cv2.imread('ima/impo.png', cv2.IMREAD_COLOR)
        ok_image = cv2.imread('ima/ok.png', cv2.IMREAD_COLOR)
        pypch_image = cv2.imread('ima/pypch.png', cv2.IMREAD_COLOR)

        time.sleep(5)

        while True:
            screen_pil = pg.screenshot()
            screen_np = np.array(screen_pil)
            screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)

            # xyz = cv2.matchTemplate(screen, xyz_image, cv2.TM_CCOEFF_NORMED)
            # xyz_min_val, xyz_max_val, xyz_min_loc, xyz_max_loc = cv2.minMaxLoc(xyz)

            sett = cv2.matchTemplate(screen, sett_image, cv2.TM_CCOEFF_NORMED)
            sett_min_val, sett_max_val, sett_min_loc, sett_max_loc = cv2.minMaxLoc(sett)

            setl = cv2.matchTemplate(screen, setl_image, cv2.TM_CCOEFF_NORMED)
            setl_min_val, setl_max_val, setl_min_loc, setl_max_loc = cv2.minMaxLoc(setl)

            threshold = 0.8

            if setl_max_val >= threshold:
                match_x, match_y = setl_max_loc
                # print("Template found at:", match_x, match_y)
                pg.moveTo(match_x + 10, match_y + 10, 0.00000000000001)
                pg.click(button='left')
                if sett_max_val >= threshold:
                    match_x, match_y = sett_max_loc
                    pg.moveTo(match_x + 10, match_y + 10, 0.00000000000001)
                    pg.click(button='left')
                    time.sleep(0.5)
                    cv2.destroyAllWindows()

                    screen_pil = pg.screenshot()
                    screen_np = np.array(screen_pil)
                    screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
                    croha = cv2.matchTemplate(screen, croha_image, cv2.TM_CCOEFF_NORMED)
                    croha_min_val, croha_max_val, croha_min_loc, croha_max_loc = cv2.minMaxLoc(croha)
                    if croha_max_val >= threshold:
                        match_x, match_y = croha_max_loc
                        pg.moveTo(match_x + 15, match_y + 15, 0.00000000000001)
                        pg.click(button='left')
                        time.sleep(0.5)
                        cv2.destroyAllWindows()

                        screen_pil = pg.screenshot()
                        screen_np = np.array(screen_pil)
                        screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
                        impo = cv2.matchTemplate(screen, impo_image, cv2.TM_CCOEFF_NORMED)
                        impo_min_val, impo_max_val, impo_min_loc, impo_max_loc = cv2.minMaxLoc(impo)
                        if impo_max_val >= threshold:
                            match_x, match_y = impo_max_loc
                            pg.moveTo(match_x + 10, match_y + 10, 0.00000000000001)
                            pg.click(button='left')
                            time.sleep(0.5)
                            cv2.destroyAllWindows()
                            screen_pil = pg.screenshot()
                            screen_np = np.array(screen_pil)
                            screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
                            pypch = cv2.matchTemplate(screen, pypch_image, cv2.TM_CCOEFF_NORMED)
                            pypch_min_val, pypch_max_val, pypch_min_loc, pypch_max_loc = cv2.minMaxLoc(pypch)
                            if pypch_max_val >= threshold:
                                match_x, match_y = pypch_max_loc
                                pg.moveTo(match_x + 90, match_y + 140, 0.00000000000001)
                                pg.click(button='left')
                                pg.write(c)
                                pg.press("backspace")
                                pg.moveTo(match_x + 97, match_y + 300, 0.00000000000001)
                                pg.click(button='left')
                                cv2.destroyAllWindows()
                                time.sleep(1)
                                screen_pil = pg.screenshot()
                                screen_np = np.array(screen_pil)
                                screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
                                ok = cv2.matchTemplate(screen, ok_image, cv2.TM_CCOEFF_NORMED)
                                ok_min_val, ok_max_val, ok_min_loc, ok_max_loc = cv2.minMaxLoc(ok)
                                if ok_max_val >= threshold:
                                    match_x, match_y = ok_max_loc
                                    pg.moveTo(match_x + 10, match_y + 10, 0.00000000000001)
                                    pg.click(button='left')
                                    text_label = ctk.CTkLabel(self.cross_view_box,text=f"Crosshair has been added successfully!")
                                    text_label.pack(side="top", padx=5, pady=5)
                                    break
                                else:
                                    text_label = ctk.CTkLabel(self.cross_view_box,text=f"Crosshair code is incorrect .Please correct it from previous menu")
                                    text_label.pack(side="top", padx=5, pady=5)
                                    break
                            else:
                                text_label = ctk.CTkLabel(self.cross_view_box,text=f"Your all Crosshair slots are full")
                                text_label.pack(side="top", padx=5, pady=5)
                                break
            cv2.destroyAllWindows()
pass

def run():
    app = CrosshairManager()
    app.root.mainloop()

if __name__ == "__main__":
    run()
