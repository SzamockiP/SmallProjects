import pyautogui, time
time.sleep(5)
print("Writing")
f = open("Tekst.txt", "r", encoding='UTF8')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(0.5)
    print(word)
print("Ended")
f.close()
