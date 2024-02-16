import tkinter as tk
import hashlib
def create_frames():
    root = tk.Tk()
    root.title("Three Frames Example")

    # First Frame (increased height)
    frame1 = tk.Frame(root, bg="red", height=100)  # Adjust the height as needed
    frame1.grid(row=0, column=0, columnspan=2, sticky="ew")
    label1 = tk.Label(frame1, text="Frame 1 - Full Width",font=("Helvetica", 50, "bold"), fg="white", bg="red")
    label1.pack(fill=tk.BOTH, expand=True)

    # Second Frame (left half)
    frame2 = tk.Frame(root, bg="green", height=50)
    frame2.grid(row=1, column=0, sticky="nsew")
    label2 = tk.Label(frame2, text="Frame 2 - Left Half", fg="white", bg="green")
    label2.pack(fill=tk.BOTH, expand=True)

    # Third Frame (right half)
    frame3 = tk.Frame(root, bg="blue", height=50)
    frame3.grid(row=1, column=1, sticky="nsew")
    label3 = tk.Label(frame3, text="Frame 3 - Right Half", fg="white", bg="blue")
    label3.pack(fill=tk.BOTH, expand=True)

    # Set grid weights to allow resizing
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.mainloop()

# Run the GUI
# create_frames()

def hashPassword(Password):
    hasher = hashlib.new('md5')
    hasher.update(Password)
    hashedPassword = hasher.digest()
    return hashedPassword


print(hashPassword("vishnu".encode()))



