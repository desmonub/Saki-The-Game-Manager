import customtkinter as ctk
import Valorant_Manager as vm
import Crosshair_Manager as cm
import Agent_Selction as ags
import Steam_Manager as sm
import setting as si

class GameManager():
    def __init__(self):
        # Load settings
        self.settings = si.set.load_settings()
        self.root = ctk.CTk()
        self.root.iconbitmap('ima/logo.ico')
        window_width = 850
        window_height = 450
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the geometry of the window to center it
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.root.title("Saki The Game Manager")

        # Set the minimum and maximum size of the window
        self.root.minsize(850, 450)  # Minimum size (width, height)
        self.root.maxsize(1050, 550)  # Maximum size (width, height)

        # Apply settings
        ctk.set_appearance_mode(self.settings['appearance_mode'])
        ctk.set_widget_scaling(self.settings['scaling'])

        # Create main label
        self.main_label = ctk.CTkLabel(self.root, text="Saki", font=("Roman", 54))
        self.main_label.pack(pady=10)

        # Create a central frame
        self.central_frame = ctk.CTkFrame(self.root, border_width=1)
        self.central_frame.pack(padx=20, pady=20)

        # Create frames inside the central frame
        self.left_frame = ctk.CTkFrame(self.central_frame, border_width=1)
        self.left_frame.grid(row=0, column=0, padx=40, pady=40, sticky="nsew")

        self.right_frame = ctk.CTkFrame(self.central_frame, border_width=1)
        self.right_frame.grid(row=0, column=1, padx=40, pady=40, sticky="nsew")

        self.central_frame.grid_columnconfigure(0, weight=1)
        self.central_frame.grid_columnconfigure(1, weight=1)

        # Add title and buttons to the left frame
        self.valorant_title = ctk.CTkLabel(self.left_frame, text="Valorant Manager", font=("Helvetica", 17))
        self.valorant_title.pack(pady=10)

        self.valorant_button = ctk.CTkButton(self.left_frame, text="ID Management", command=self.open_valorant_manager)
        self.valorant_button.pack(pady=10)

        self.crosshair_button = ctk.CTkButton(self.left_frame, text="Crosshair Management", command=self.open_crosshair_manager)
        self.crosshair_button.pack(pady=5)

        self.agent_button = ctk.CTkButton(self.left_frame, text="Agent Selection", command=self.open_agent_selection)
        self.agent_button.pack(pady=10)

        # Add title and button to the right frame
        self.steam_title = ctk.CTkLabel(self.right_frame, text="Steam Manager", font=("Helvetica", 17))
        self.steam_title.pack(pady=10)

        self.steam_button = ctk.CTkButton(self.right_frame, text="ID Management", command=self.open_steam_manager)
        self.steam_button.pack(pady=10)

        # Add settings button to the bottom right
        self.setting_button = ctk.CTkButton(self.root, text="Settings", command=self.open_settings)
        self.setting_button.pack(side="bottom", anchor="e", pady=10)

    def open_valorant_manager(self):
        vm.run()

    def open_crosshair_manager(self):
        cm.run()

    def open_agent_selection(self):
        ags.run(self.root)

    def open_steam_manager(self):
        sm.run()

    def open_settings(self):
        si.run()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = GameManager()
    app.run()
