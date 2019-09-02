import keyboard

def main():
    keyboard.write("print('Hello world!')")
    keyboard.wait("esc")
    print("Hello world")

if __name__ == '__main__':
    main()