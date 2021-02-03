sound_level = float(input("Enter the sound level in decibel: "))

jackhammer = 130
gas_lawnmower = 106
alarm_clock = 70
quiet_room = 40

if sound_level == jackhammer:
    print("The sound level entered equals to a jackhammer sound level.")
elif sound_level == gas_lawnmower:
    print("The sound level entered equals to a gas lawnmower sound level.")
elif sound_level == alarm_clock:
    print("The sound level entered equals to a alarm clock sound level.")
elif sound_level == quiet_room:
    print("The sound level entered equals to a quiet room sound level.")
elif sound_level > jackhammer:
    print("The sound level entered is higher than a jackhammer sound level.")
elif sound_level < quiet_room:
    print("The sound level entered is lower than a quiet room sound level.")
elif sound_level >= gas_lawnmower and sound_level <= jackhammer:
    print("The sound level entered is between a jackhammer and a gas lawnmower sound level.")
elif sound_level >= alarm_clock and sound_level <= gas_lawnmower:
    print("The sound level entered is between an alarm clock and a gas lawnmower sound level.")
elif sound_level >= quiet_room and sound_level <= alarm_clock:
    print("The sound level entered is between an alarm clock and a quiet room sound level.")