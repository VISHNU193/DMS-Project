import tkinter as tk
from tkinter import filedialog, simpledialog
from cryptography.fernet import Fernet

class FileEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryptor")

        self.key_filename = 'secret.key'
        self.load_or_generate_key()

        # Create GUI elements
        self.label = tk.Label(root, text="Select File:")
        self.label.pack(pady=10)

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_file)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_file)
        self.decrypt_button.pack(pady=5)

    def load_or_generate_key(self):
        try:
            self.key = load_key(self.key_filename)
        except FileNotFoundError:
            self.key = generate_key()
            save_key(self.key, self.key_filename)

    def get_password(self):
        return simpledialog.askstring("Password", "Enter Password:", show='*')

    def encrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            password = self.get_password()
            if password:
                key = Fernet.generate_key()
                cipher = Fernet(key)
                with open(file_path, 'rb') as file:
                    data = file.read()
                encrypted_data = cipher.encrypt(data)
                with open(file_path, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted_data)
                save_key(key, file_path + '_key.key')
                tk.messagebox.showinfo("Encryption", "File encrypted successfully!")

    def decrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            password = self.get_password()
            if password:
                key_filename = file_path + '_key.key'
                key = load_key(key_filename)
                cipher = Fernet(key)
                with open(file_path, 'rb') as encrypted_file:
                    encrypted_data = encrypted_file.read()
                decrypted_data = cipher.decrypt(encrypted_data)
                with open(file_path, 'wb') as decrypted_file:
                    decrypted_file.write(decrypted_data)
                tk.messagebox.showinfo("Decryption", "File decrypted successfully!")


root = tk.Tk()
app = FileEncryptorApp(root)
root.mainloop()
