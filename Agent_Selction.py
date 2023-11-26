import cv2
import numpy as np
import pyautogui as pg
import threading
from PIL import Image
import time
import customtkinter as ctk

class AgentSelection():
    def __init__(self, parent):
        # Create the main window
        self.root = ctk.CTkToplevel(parent)
        self.root.after(250, lambda: self.root.iconbitmap('ima/logo.ico'))
        window_width = 810
        window_height = 650
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the geometry of the window to center it
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.root.title("Agent Selection")

        # Make the window non-resizable
        self.root.minsize(810, 650)  # Minimum size (width, height)
        self.root.maxsize(980, 750)  # Maximum size (width, height)

        self.stop_process = False

        # Create a main frame
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill='both', expand=True)

        # Create a frame for the Cancel button and the status label
        self.bottom_frame = ctk.CTkFrame(self.root)
        self.bottom_frame.pack(fill='both', expand=True)

        # Add a Cancel button to the bottom frame
        self.cancel_button = ctk.CTkButton(self.bottom_frame, text="Cancel Agent Selection", command=self.cancel_aglock, hover_color="#000080")
        self.cancel_button.pack(pady=10)

        # Add a status label to the bottom frame
        self.status_label = ctk.CTkLabel(self.bottom_frame, text="")
        self.status_label.pack(padx=10, pady=10)

        # Add 23 image buttons to the main frame
        self.agent_images = {
            "Astra": 'ima/agents/astra.png',
            "Breach": 'ima/agents/breach.png',
            "Brimstone": 'ima/agents/brimstone.png',
            "Chamber": 'ima/agents/chamber.png',
            "Cypher": 'ima/agents/cypher.png',
            "Deadlock": 'ima/agents/deadlock.png',
            "Fade": 'ima/agents/fade.png',
            "Gekko": 'ima/agents/gekko.png',
            "Harber": 'ima/agents/harbor.png',
            "Iso": 'ima/agents/iso.png',
            "Jett": 'ima/agents/jett.png',
            "Kay/O": 'ima/agents/kayo.png',
            "Killjoy": 'ima/agents/killjoy.png',
            "Neon": 'ima/agents/neon.png',
            "Omen": 'ima/agents/omen.png',
            "Phoenix": 'ima/agents/phoenix.png',
            "Raze": 'ima/agents/raze.png',
            "Reyna": 'ima/agents/reyna.png',
            "Sage": 'ima/agents/sage.png',
            "Skye": 'ima/agents/skye.png',
            "Sova": 'ima/agents/sova.png',
            "Viper": 'ima/agents/viper.png',
            "Yoru": 'ima/agents/yoru.png'
        }
        for i, (agent, image_path) in enumerate(self.agent_images.items()):
            row, col = divmod(i, 7)
            self.ag_button(self.main_frame, agent, image_path, row, col)

    def ag_button(self, frame, agent_name, original_image_path, row, col):
        blurred_image_path = original_image_path.replace("ima/agents/", "ima/stickers/")
        light_image = Image.open(blurred_image_path)
        dark_image = Image.open(blurred_image_path)
        my_image = ctk.CTkImage(light_image=light_image, dark_image=dark_image, size=(100, 100))

        # Create a PhotoImage instance right before creating the CTkButton instance
        image_button = ctk.CTkButton(self.main_frame, image=my_image, text=agent_name, compound='top', height=10, width=10, hover_color="#000080")
        image_button.grid(row=row, column=col, padx=1, pady=1)  # Adjust padx and pady as needed
        image_button.bind("<Button-1>",lambda event, name=agent_name, path=original_image_path: self.thread_agent(name, path))

    def thread_agent(self, agent, image_path):
        threading.Thread(target=self.ag_button_click, args=(agent, image_path)).start()

    def ag_button_click(self, agent,original_image_path):
        self.stop_process = False
        self.status_label.configure(text=f"Selected agent: {agent}")
        template_image = cv2.imread(original_image_path, cv2.IMREAD_COLOR)
        li = cv2.imread('ima/lock_in.png', cv2.IMREAD_COLOR)
        while not self.stop_process:
            screen_np = np.array(pg.screenshot(region=(0, pg.size()[1] // 2, pg.size()[0], pg.size()[1] // 2)))
            screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
            result = cv2.matchTemplate(screen, template_image, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)
            result2 = cv2.matchTemplate(screen, li, cv2.TM_CCOEFF_NORMED)
            _, _, _, max_loc2 = cv2.minMaxLoc(result2)
            if max_val >= 0.8:
                pg.click(x=max_loc[0] + 41, y=max_loc[1] + pg.size()[1] // 2 + 32, button='left')
                time.sleep(0.2)
                pg.click(x=max_loc2[0] + 30, y=max_loc2[1] + pg.size()[1] // 2 + 30, button='left')
                self.status_label.configure(text="Agent lock successful")
                break
        cv2.destroyAllWindows()

    def cancel_aglock(self):
        self.stop_process = True
        self.status_label.configure(text="Agent lock canceled")

def run(parent):
    app = AgentSelection(parent)
    app.root.mainloop()

if __name__ == "__main__":
    run()