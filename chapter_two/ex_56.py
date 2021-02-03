choice = input("Are you using Hz, KHz, MHz or GHz? ")
choice = choice.lower()

if choice == "hz":
    freq = float(input("Enter the frequency in Hz: "))
elif choice == "khz":
    khz = float(input("Enter the frequency in KHz: "))
    freq = khz * 10 ** 3
elif choice == "mhz":
    mhz = float(input("Enter the frequency in MHz: "))
    freq = mhz * 10 ** 6
elif choice == "ghz":
    ghz = float(input("Enter the frequency in GHz: "))
    freq = ghz * 10 ** 9

name = " "

if freq < 3 * 10 ** 9:
    name = "Radio Waves"
elif 3 * 10 ** 9 <= freq < 3 * 10 ** 12:
    name = "Microwave"
elif 3 * 10 ** 12 <= freq < 4.3 * 10 ** 14:
    name = "Infrared Light"
elif 4.3 * 10 ** 14 <= freq < 7.5 * 10 ** 14:
    name = "Visible Light"
elif 7.5 * 10 ** 14 <= freq < 3 * 10 ** 17:
    name = "Ultraviolet Light"
elif 3 * 10 ** 17 <= freq < 3 * 10 ** 19:
    name = "X-Rays"
elif freq > 3 * 10 ** 19:
    name = "Gamma rays"

if name == " ":
    print("Error, invalid value.")
else:
    print(f"The radiaton name related to the frequency entered is: {name}.")
