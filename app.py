
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import json
import os

class ContactNotebook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Notebook")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.contacts = []

        # Title
        tk.Label(root, text="Contact Notebook", font=("Arial", 18, "bold")).pack(pady=10)

        # Listbox for contacts
        self.listbox = tk.Listbox(root, width=60, height=10)
        self.listbox.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack()

        tk.Button(button_frame, text="Add Contact", width=15, command=self.add_contact).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Delete Contact", width=15, command=self.delete_contact).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(button_frame, text="Save Contacts", width=15, command=self.save_contacts).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="Load Contacts", width=15, command=self.load_contacts).grid(row=1, column=1, padx=5, pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Name", "Enter contact name:")
        if not name:
            return
        phone = simpledialog.askstring("Phone", "Enter phone number:")
        if not phone:
            return
        contact = {"name": name, "phone": phone}
        self.contacts.append(contact)
        self.update_listbox()

    def delete_contact(self):
        try:
            selected_index = self.listbox.curselection()[0]
            del self.contacts[selected_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def save_contacts(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                 filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, "w") as f:
                json.dump(self.contacts, f)
            messagebox.showinfo("Saved", "Contacts saved successfully!")

    def load_contacts(self):
        file_path = filedialog.askopenfilename(defaultextension=".json",
                                               filetypes=[("JSON files", "*.json")])
        if file_path and os.path.exists(file_path):
            with open(file_path, "r") as f:
                self.contacts = json.load(f)
            self.update_listbox()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactNotebook(root)
    root.mainloop()
