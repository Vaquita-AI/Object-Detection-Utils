import os, re
import time
import pyautogui
from PIL import Image
import keyboard

# Define the directory where you want to save the images
save_directory = r"C:\Users\Vaquita\Downloads\Valomalo\selected_images"

# Ensure the save directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

def capture_and_save_image():
    # Capture the screen
    screenshot = pyautogui.screenshot()

    # Define the file name with a timestamp
    file_name = f"image_{int(time.time())}.jpg"
    file_path = os.path.join(save_directory, file_name)

    # Save the screenshot
    screenshot.save(file_path)
    print(f"Image saved to {file_path}")

# Define the hotkey combination
hotkey = 'num 0'

# Register the hotkey
keyboard.add_hotkey(hotkey, capture_and_save_image)

print(f"Press {hotkey} to capture and save the image.")

# Keep the script running
keyboard.wait('ctrl+esc')  # Press 'esc' to exit the script