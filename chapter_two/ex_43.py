C4_freq = 261.63
D4_freq = 293.66
E4_freq = 329.63
F4_freq = 349.23
G4_freq = 392.00
A4_freq = 440.00
B4_freq = 493.88

limit = 1

freq = float(input("enter the frequency in Hz: "))

if freq >= C4_freq - limit and freq <= C4_freq + limit:
    note = "C4"
elif freq >= D4_freq - limit and freq <= D4_freq + limit:
    note = "D4"
elif freq >= E4_freq - limit and freq <= E4_freq + limit:
    note = "E4"
elif freq >= F4_freq - limit and freq <= F4_freq + limit:
    note = "F4"
elif freq >= G4_freq - limit and freq <= G4_freq + limit:
    note = "G4"
elif freq >= A4_freq - limit and freq <= A4_freq + limit:
    note = "A4"
elif freq >= B4_freq - limit and freq <= C4_freq + limit:
    note = "B4"

note = " "

if note == " ":
    print("No note for that frequency.")
else:
    print(f"That frequency is {note}")