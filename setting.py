import json
import customtkinter as ctk

class set(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Load settings from file
        self.settings = self.load_settings()

        # Configure window
        window_width = 250
        window_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Set the geometry of the window to center it
        self.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.title("Settings")
        self.iconbitmap('ima/logo.ico')

        # Set the minimum and maximum size of the window
        self.minsize(250, 200)  # Minimum size (width, height)
        self.maxsize(1050, 450)  # Maximum size (width, height)

        # Add Appearance Mode Label and OptionMenu
        appearance_mode_label = ctk.CTkLabel(self, text="Appearance Mode:", anchor="w")
        appearance_mode_label.grid(row=0, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(self, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionmenu.grid(row=1, column=0, padx=20, pady=(10, 5))
        self.appearance_mode_optionmenu.set(self.settings['appearance_mode'])

        # Add UI Scaling Label and OptionMenu
        scaling_label = ctk.CTkLabel(self, text="UI Scaling:", anchor="w")
        scaling_label.grid(row=2, column=0, padx=20, pady=(5, 0))
        self.scaling_optionmenu = ctk.CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionmenu.grid(row=3, column=0, padx=20, pady=(5, 5))
        self.scaling_optionmenu.set(f"{int(self.settings['scaling']*100)}%")

    @staticmethod
    def load_settings():
        try:
            with open('settings.json', 'r') as f:
                if f.read().strip():
                    # Reset the file pointer to the beginning
                    f.seek(0)
                    settings = json.load(f)
                else:
                    # If the file is empty, write default settings to it
                    settings = {'appearance_mode': 'System', 'scaling': 1.0}
                    with open('settings.json', 'w') as f:
                        json.dump(settings, f)
        except FileNotFoundError:
            # If the settings file doesn't exist, create it with default settings
            settings = {'appearance_mode': 'System', 'scaling': 1.0}
            with open('settings.json', 'w') as f:
                json.dump(settings, f)
        return settings

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
        self.save_setting('appearance_mode', new_appearance_mode)
        self.save_setting('settings_changed', True)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)
        self.save_setting('scaling', new_scaling_float)

    def save_setting(self, setting, value):
        with open('settings.json', 'r') as f:
            settings = json.load(f)
        settings[setting] = value
        with open('settings.json', 'w') as f:
            json.dump(settings, f)

def run():
    app = set()
    app.mainloop()

if __name__ == "__main__":
    run()
