import easyocr, subprocess, time, cv2
subprocess.run("adb tcpip 5555")
inp = input("Enter ip address: ")
min_trophy = 30  # Minmun trophy to stop the script
if inp == "":
    inp = "192.0.0.2"
subprocess.run(f"adb connect {inp}:5555")
reader = easyocr.Reader(['en'])
print("Starting...")
subprocess.run(r"adb shell input tap 189 910", stdout=subprocess.DEVNULL)
time.sleep(0.2)
subprocess.run(r"adb shell input tap 1720 666", stdout=subprocess.DEVNULL)
flag = 0
while True:
    flag += 1
    if flag > 5:
        subprocess.run(r"adb shell input tap 2151 756", stdout=subprocess.DEVNULL)
        flag = 0
    time.sleep(2)
    subprocess.run(r"adb shell screencap -p /sdcard/screen.png", stdout=subprocess.DEVNULL)
    subprocess.run(r"adb pull /sdcard/screen.png screen.png", stdout=subprocess.DEVNULL)
    img = cv2.imread(r"screen.png")[316:383, 103:255]
    try:
        out = int(reader.readtext(img)[0][1])
        flag = 0
        print(out, flush=True)
        if out < min_trophy:
            subprocess.run(r"adb shell input tap 2151 756", stdout=subprocess.DEVNULL)
            subprocess.run(r"adb shell input tap 2151 756", stdout=subprocess.DEVNULL)
        elif min_trophy <  out:
            subprocess.run('''PowerShell -Command "Add-Type -AssemblyName PresentationFramework;[System.Windows.MessageBox]::Show('Good Base found!')"
''')

    except:
        pass
