import tkinter as tk
from tkinter import filedialog, simpledialog, ttk, messagebox
from cryptography.fernet import Fernet
from argon2 import hash_password,hash_password_raw
from bcrypt import *
from hashlib import *
class FileEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryptor")

        self.key_filename = 'secret.key'
        self.load_or_generate_key()

        
    

            # First Frame (increased height)
        frame1 = tk.Frame(root, bg="white", height=100)  # Adjust the height as needed
        frame1.grid(row=0, column=0, columnspan=2, sticky="ew")
        # label1 = tk.Label(frame1, text="Frame 1 - Full Width",font=("Helvetica", 50, "bold"), fg="white", bg="red")
        # label1.pack(fill=tk.BOTH, expand=True)
        label2_text = "ENCRYPTION : \n\n\n(1)Choose a Symmetric Key: Select a secret key that will be used for both \nencryption and decryption.\nThis key should be kept confidential and shared securely between the sender and the recipient.\n\n(2)Select an Encryption Algorithm: There are various symmetric encryption algorithms available,\n such as AES (Advanced Encryption Standard), DES (Data Encryption Standard), and Blowfish.\n Choose one that suits your requirements in terms of security and performance.\n\n(3)Encrypt the Data: To encrypt your data, use the \nchosen encryption algorithm along with the symmetric key.\nApply the algorithm to the plaintext data along with the key to produce ciphertext.\n\n(4)Transmit or Store the Encrypted Data: Share the encrypted data \nwith the intended recipient or store it securely.\nSince symmetric encryption uses the same key for \nencryption and decryption, make sure the recipient has the key to decrypt the data.\n\n(5)Decrypt the Data: When the recipient receives the encrypted data,\nthey can decrypt it using the same symmetric key that was used for encryption.\nApply the decryption algorithm with the shared key to recover the original plaintext data.\n\n(6)Ensure Security of the Key: Keep the symmetric\nkey secure during transmission and storage.\nUse secure channels for key exchange, such as asymmetric encryption (e.g., RSA)\nor key exchange protocols like Diffie-Hellman, to prevent unauthorized access to the key.\n\n(7)Use Proper Key Management: Rotate keys periodically, especially\nif they might have been compromised.\nEnsure that keys are generated securely and are\nof sufficient length to resist brute-force attacks.\n"
#         # Second Frame (left half)
        frame2 = tk.Frame(root, bg="black", height=50)
        frame2.grid(row=1, column=0, sticky="nsew")
        label2 = tk.Label(frame2, text=label2_text, fg="#2448b5", bg="white",font=("Helvetica", 10, "bold"))
        label2.pack(fill=tk.BOTH, expand=True)

        label3_text="DECRYPTION :\n\n\n(1)Obtain the Encrypted Data: Start with the encrypted data that you want to decrypt.\n This data should have been encrypted using a\n symmetric encryption algorithm with a specific secret key.\n\n(2)Acquire the Symmetric Key: You need the same secret key that was\nused for encryption in order to decrypt the data successfully.\nEnsure that you have access to this key.\n\n(3)Select the Decryption Algorithm: Choose the same symmetric encryption\nalgorithm that was used for encryption.Ensure that you\nhave a compatible decryption implementation for this algorithm.\n\n(4)Apply Decryption: Use the chosen decryption algorithm along with the symmetric\nkey to decrypt the encrypted data.Apply the algorithm to the ciphertext\nalong with the key to obtain the original plaintext.\n\n(5)Retrieve the Decrypted Data: Once the decryption process is complete, \nyou will have the original plaintext data that was encrypted.This data is now in its original, human-readable form.\n\n(6)Handle the Decrypted Data: Process, store, or transmit the decrypted data as needed for your application.\nEnsure that appropriate\nsecurity measures are in place to protect the data\'s confidentiality and integrity."

        l3_text="""
        1. Obtain the Encrypted Data: Start with the encrypted data that you want to decrypt. This data should have been encrypted using a symmetric encryption algorithm with a specific secret key.

        2. Acquire the Symmetric Key: You need the same secret key that was used for encryption in order to decrypt the data successfully. Ensure that you have access to this key.

        3. Select the Decryption Algorithm: Choose the same symmetric encryption algorithm that was used for encryption. Ensure that you have a compatible decryption implementation for this algorithm.

        4. Apply Decryption: Use the chosen decryption algorithm along with the symmetric key to decrypt the encrypted data. Apply the algorithm to the ciphertext along with the key to obtain the original plaintext.

        5. Retrieve the Decrypted Data: Once the decryption process is complete, you will have the original plaintext data that was encrypted. This data is now in its original, human-readable form.

        6. Handle the Decrypted Data: Process, store, or transmit the decrypted data as needed for your application. Ensure that appropriate security measures are in place to protect the data's confidentiality and integrity.
        """

    

        # Third Frame (right half)
        frame3 = tk.Frame(root, bg="black", height=50)
        frame3.grid(row=1, column=1, sticky="nsew")
        label3 = tk.Label(frame3, text=label3_text, fg="purple", bg="white",font=("Helvetica", 10, "bold"))
        label3.pack(fill=tk.BOTH, expand=True)

        # Set grid weights to allow resizing
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

        
        # Create a Label widget
        label_text = "FILE Encryptor"
        label = tk.Label(frame1, text=label_text,font=("Helvetica", 50, "bold"),bg="white")

        # Pack the Label widget into the main window
        label.pack()

        # Create GUI elements
        self.label = tk.Label(frame1, text="Select File:",font=("Helvetica", 15, "bold") ,bg="white")
        self.label.pack(pady=10)

        self.encrypt_button = tk.Button(frame1, text="Encrypt a file",font=("Helvetica", 12, "bold") , command=self.encrypt_file)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = tk.Button(frame1, text="Decrypt a file",font=("Helvetica", 12, "bold",) ,fg="black",command=self.decrypt_file)
        self.decrypt_button.pack(pady=10)
        
        self.password =""

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
            password = hashPassword(self.get_password().encode())
            write_password(password,file_path)
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
             
            new_password = str(hashPassword(self.get_password().encode()))
            actual_password = read_password(file_path)
            if new_password == actual_password:
                key_filename = file_path + '_key.key'
                key = load_key(key_filename)
                cipher = Fernet(key)
                with open(file_path, 'rb') as encrypted_file:
                    encrypted_data = encrypted_file.read()
                decrypted_data = cipher.decrypt(encrypted_data)
                with open(file_path, 'wb') as decrypted_file:
                    decrypted_file.write(decrypted_data)
                tk.messagebox.showinfo("Decryption", "File decrypted successfully!")
            else:
                tk.messagebox.showinfo("Incorrect password!!","Incorrect password!!")

def generate_key():
    return Fernet.generate_key()

def save_key(key, key_filename):
    with open(key_filename, 'wb') as key_file:
        key_file.write(key)

def write_password(password,filename):
    with open("C:/All code/DMS-Project/dms/password.txt","a") as pw_file:
        pw_file.write(filename+"@"+str(password)+"\n")
    return
def read_password(filename):
    with open("C:/All code/DMS-Project/dms/password.txt","r") as pw_file:
        text = pw_file.readlines()
        for iter in text:
            #print(iter)
            if(iter.find(filename)!=-1):
                s=iter.rstrip("\n")
                item_list = s.split("@")
                with open('C:/All code/DMS-Project/dms/password.txt', 'w') as fw:
                    for line in text:
                        if line.find(filename)==-1:
                            fw.write(line)
                return item_list[1]
    return ""


def load_key(key_filename):
    return open(key_filename, 'rb').read()

def hashPassword(Password):
    hasher = new('md5')
    hasher.update(Password)
    hashedPassword = hasher.digest()
    return hashedPassword


if __name__ == "__main__":
    root = tk.Tk()
    app = FileEncryptorApp(root)
    root.mainloop()

# print(hashPassword("123456".encode()))