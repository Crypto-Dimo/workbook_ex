wavelength = float(input("Enter the light's wavelength: "))

spectrum = " "

if 380 <= wavelength < 450:
    spectrum = "violet"
elif 450 <= wavelength < 495:
    spectrum = "blue"
elif 495 <= wavelength < 570:
    spectrum = "green"
elif 570 <= wavelength < 590:
    spectrum = "yellow"
elif 590 <= wavelength < 620:
    spectrum = "orange"
elif 620 <= wavelength <= 750:
    spectrum = "red"

if spectrum == " ":
    print("The wavelength is outside of the visible spectrum.")
else:
    print(f"The spectrum related to the entered wavelength is {spectrum}.")