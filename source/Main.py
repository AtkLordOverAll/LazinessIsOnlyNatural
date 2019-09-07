import keyboard

def main():
    keyboard.add_hotkey("space", print, args = ["Space was pressed"])
    keyboard.add_hotkey("alt", keyboard.write, args = ["Alt was pressed"])
    #keyboard.write("print('Hello world!')")
    keyboard.wait("esc")
    print("Hello world")

if __name__ == '__main__':
    main()