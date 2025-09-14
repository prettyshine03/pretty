import tkinter as tk
from PIL import Image, ImageTk
import os

# Automatically create output folder if it doesn't exist
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"✅ Created folder: {output_folder}")
else:
    print(f"📁 Folder already exists: {output_folder}")

# Create main window
root = tk.Tk()
root.title("Champion Announcement")
root.geometry("800x600")
root.configure(bg="#a020f0")  # Purple background

# Top text
top_label = tk.Label(
    root,
    text="MC : AND THE OVERALL CHAMPION IS CCJ\nKNIGHTS !!!",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#a020f0"
)
top_label.pack(pady=(40, 20))

# Subtext
subtext_label = tk.Label(
    root,
    text="Us :",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#a020f0"
)
subtext_label.pack()

# Load and resize image for display only (no saving)
image_path = "image.jpg"  # Change this to your image filename
img = Image.open(image_path)
img = img.resize((700, 300), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(img)

# Display image
image_label = tk.Label(root, image=photo, bg="#a020f0")
image_label.pack(pady=20)

# Run the GUI loop
root.mainloop()
