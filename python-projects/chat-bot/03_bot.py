import pyautogui
import pyperclip
import time
from openai import OpenAI

client = OpenAI(
    api_key="sk-your-real-api-key-here",
)

# Small delay to give you time to switch to the target window
time.sleep(2)

# Step 1: Click on the icon
pyautogui.click(1374, 1040)
time.sleep(1)

# Step 2: Drag to select text
pyautogui.moveTo(527, 187)
pyautogui.dragTo(1878, 922, duration=1, button='left')

time.sleep(0.5)              # allow selection to complete
pyautogui.click(1878, 922)   # focus window
time.sleep(0.3)

# Step 3: Copy selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)              # allow clipboard update

# Step 4: Get text from clipboard into variable
chat_history = pyperclip.paste()

print("Copied Text:")
print(chat_history)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are person named harry who speaks hindi as well as english. He is from India and his is a coder. You analyzed chat history and respond like harry"
        },
        {
            "role": "user",
            "content": chat_history
        }
    ]
)

response = completion.choices[0].message.content
pyperclip.copy(response)

pyautogui.click(1001, 977)
time.sleep(1)

# Paste text
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Press Enter
pyautogui.press('enter')
