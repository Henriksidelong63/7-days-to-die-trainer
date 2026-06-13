import tkinter as tk
from tkinter import messagebox
from trainer import SevenDaysTrainer

class TrainerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("7 Days to Die Trainer")
        self.root.geometry("300x200")

        self.trainer = SevenDaysTrainer()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="7 Days to Die Trainer", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="Set Health to 1000", command=self.set_health).pack(pady=5)
        tk.Button(self.root, text="Set Stamina to 100", command=self.set_stamina).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=20)

    def set_health(self):
        if self.trainer.set_health():
            messagebox.showinfo("Success", "Health set to 1000!")
        else:
            messagebox.showerror("Error", "Failed to set health. Is the game running?")

    def set_stamina(self):
        if self.trainer.set_stamina():
            messagebox.showinfo("Success", "Stamina set to 100!")
        else:
            messagebox.showerror("Error", "Failed to set stamina. Is the game running?")

    def run(self):
        self.root.mainloop()
        self.trainer.close()