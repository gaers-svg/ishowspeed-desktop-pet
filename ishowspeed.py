import urllib.request
import tkinter as tk
from PIL import Image, ImageTk
import os
import random
from io import BytesIO
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# -------------------------
# Main Clickable Image Setup
# -------------------------

# Download main image
img_url = "https://raw.githubusercontent.com/gaers-svg/ishowspeed-desktop-pet/main/Screenshot_22-3-2026_115654_www.youtube.com.png"
img_file = "Screenshot.png"
urllib.request.urlretrieve(img_url, img_file)

# Download main click sound
sound_url = "https://raw.githubusercontent.com/gaers-svg/ishowspeed-desktop-pet/main/WOOF%20WOOF.wav"
sound_file = "WOOF WOOF.wav"
if not os.path.exists(sound_file):
    urllib.request.urlretrieve(sound_url, sound_file)

# Download SpongeBob sound
sound_url2 = "https://raw.githubusercontent.com/gaers-svg/ishowspeed-desktop-pet/main/spongbeb.wav"
sound_file2 = "spongbeb.wav"
if not os.path.exists(sound_file2):
    urllib.request.urlretrieve(sound_url2, sound_file2)

# Load image
original_img = Image.open(img_file)

# Tkinter main window
root = tk.Tk()
root.title("ishowspeed")
root.geometry("300x300")
root.resizable(False, False)

tk_img = ImageTk.PhotoImage(original_img)
label = tk.Label(root, image=tk_img)
label.pack(fill="both", expand=True)

# Resize image when window changes size
def resize_image(event):
    new_width = event.width
    new_height = event.height
    resized = original_img.resize((new_width, new_height))
    tk_img_resized = ImageTk.PhotoImage(resized)
    label.config(image=tk_img_resized)
    label.image = tk_img_resized

root.bind("<Configure>", resize_image)

# -------------------------
# Bouncing Notepad Class
# -------------------------
class BouncingNotepad:
    def __init__(self):
        # Play SpongeBob sound
        pygame.mixer.Sound(sound_file2).play()

        # Create separate window
        self.root = tk.Toplevel()
        self.root.title("hi i am spongebob :D")

        # Download image
        github_url = "https://raw.githubusercontent.com/gaers-svg/idk/main/spong.jpg"
        try:
            with urllib.request.urlopen(github_url) as response:
                image_data = response.read()
            pil_image = Image.open(BytesIO(image_data)).convert('RGBA')
        except Exception as e:
            print(f"Could not load image from GitHub: {e}")
            pil_image = Image.new("RGBA", (300, 300), (255, 0, 0, 255))

        # Resize image
        IMAGE_WIDTH = 150
        IMAGE_HEIGHT = 150
        self.pil_image = pil_image.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.Resampling.LANCZOS)

        self.photo = ImageTk.PhotoImage(self.pil_image)
        self.label = tk.Label(self.root, image=self.photo)
        self.label.image = self.photo
        self.label.pack()

        # Force update so geometry info is correct
        self.root.update_idletasks()

        # Starting position and velocity
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.x = random.randint(0, screen_width - IMAGE_WIDTH)
        self.y = random.randint(0, screen_height - IMAGE_HEIGHT)
        self.vx = 200
        self.vy = 200

        # Set initial geometry
        self.root.geometry(f"{IMAGE_WIDTH}x{IMAGE_HEIGHT}+{self.x}+{self.y}")

        # Start bouncing
        self.bounce()

    def bounce(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = self.pil_image.width
        window_height = self.pil_image.height

        self.x += self.vx
        self.y += self.vy

        # Bounce off edges
        if self.x <= 0 or self.x + window_width >= screen_width:
            self.vx = -self.vx
        if self.y <= 0 or self.y + window_height >= screen_height:
            self.vy = -self.vy

        self.root.geometry(f"+{self.x}+{self.y}")
        self.root.after(10, self.bounce)

# -------------------------
# Click handler for main image
# -------------------------
def on_image_click(event):
    # Play iShowSpeed sound
    pygame.mixer.Sound(sound_file).play()
    # Spawn bouncing SpongeBob
    for _ in range(2):
        BouncingNotepad()

label.bind("<Button-1>", on_image_click)

root.mainloop()