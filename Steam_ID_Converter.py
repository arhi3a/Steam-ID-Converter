from time import localtime, strftime

time = (strftime("%a, %d %b %Y %H:%M:%S ", localtime()))


def main_menu():
    print('1. Enter SteamID (Steam_x:x:xxxxxxxx)' '\n' '2. Enter Steam3 (U:X:XXXXXXXX)' '\n'
          '3. Enter SteamID32 (XXXXXXXX)' '\n' '4. Enter SteamID64 (XXXXXXXXXXXXXXXXX)')
    userinput1 = input('Answer:  ')
    if userinput1 == '1':  # Enter Steam ID
        SteamID_conv()
    elif userinput1 == '2':  # Enter Steam3
        Steam3_conv()
    elif userinput1 == '3':  # Enter SteamID32
        SteamID32_conv()
    elif userinput1 == '4':  # Enter SteamID64
        SteamID64_conv()
    else:
        print('Wrong number returning')
        main_menu()


def SteamID_conv():  # 1
    print('Please Enter SteamID (Steam_x:x:xxxxxxxx)')
    userinput2 = input('SteamID:  ')
    y = userinput2[8:9]  # STEAM_0:y:zzzzzz
    z = userinput2[10:]  # STEAM_0:y:zzzzzz
    Steam_ID_32_conv = int(z) * int(2) + int(y)  # Calculate steamID32
    Steam_ID_64_conv = int(Steam_ID_32_conv) + int(ID_change_value)  # Calculate SteamID64 from steamID32
    Steam_ID3 = 'U:1:' + str(Steam_ID_32_conv)  # Calculate SteamID3 from userinput and ID32
    print(pause)
    print('Steam ID:   ', userinput2)  # Print steamID from user input
    print('Steam ID3:  ', Steam_ID3)  # Print SteamID3
    print('Steam ID32: ', Steam_ID_32_conv)  # Print SteamID32
    print('Steam ID64: ', Steam_ID_64_conv)  # Print SteamID64
    print(pause)
    # Save
    userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
    if userinputx == '1':
        file = open('history.txt', 'a')
        file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) + '\n' + 'Steam ID: ' + (
        userinput2) + '\n' + 'Steam ID3: ' + (Steam_ID3) + '\n' +
                   'Steam ID32: ' + str(Steam_ID_32_conv) + '\n' + 'Steam ID64: ' + str(Steam_ID_64_conv) + '\n' + (
                       pause))
        file.close()
        main_menu()
    else:
        main_menu()


def Steam3_conv():  # 2
    print('Please Enter Steam3: (U:X:XXXXXXXX)')
    userinput5 = input('Steam3: ')
    Steam3_2_32_conv = (int(userinput5[4:]))
    Steam3_2_64_conv = int(Steam3_2_32_conv) + int(ID_change_value)
    Steam3_2_ID_conv = int(Steam3_2_32_conv) // int(2)
    print(pause)
    if (int(Steam3_2_64_conv) % 2 == 0):  # Even
        print('SteamID:   Steam_0:0:' + str(Steam3_2_ID_conv))  # Print SteamID
        print('Steam3:    ' + userinput5)  # Print Steam3 from userinput
        print('SteamID32: ' + str(Steam3_2_32_conv))  # Print SteamID32
        print('SteamID64: ' + str(Steam3_2_64_conv))  # Print SteamID64 form user input
        print(pause)
        # Save
        userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
        if userinputx == '1':
            file = open('history.txt', 'a')
            file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) +
                       '\n' + 'Steam ID: Steam_0:0:' + str(Steam3_2_ID_conv) + '\n' + 'Steam ID3: ' + (
                       userinput5) + '\n' +
                       'Steam ID32: ' + str(Steam3_2_32_conv) + '\n' + 'Steam ID64: ' + str(Steam3_2_64_conv) +
                       '\n' + (pause))
            file.close()
            main_menu()
        else:
            main_menu()
    else:  # Odd
        print('SteamID:   Steam_0:1:' + str(Steam3_2_ID_conv))  # Print SteamID
        print('Steam3:    ' + userinput5)  # Print Steam3 from userinput
        print('SteamID32: ' + str(Steam3_2_32_conv))  # Print SteamID32
        print('SteamID64: ' + str(Steam3_2_64_conv))  # Print SteamID64 form user input
        print(pause)
        # Save
        userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
        if userinputx == '1':
            file = open('history.txt', 'a')
            file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) +
                       '\n' + 'Steam ID: Steam_0:1:' + str(Steam3_2_ID_conv) + '\n' + 'Steam ID3: ' + (
                       userinput5) + '\n' +
                       'Steam ID32: ' + str(Steam3_2_32_conv) + '\n' + 'Steam ID64: ' + str(Steam3_2_64_conv) +
                       '\n' + (pause))
            file.close()
            main_menu()
        else:
            main_menu()


def SteamID32_conv():  # 3
    print('Please Enter SteamID32 (XXXXXXXX)')
    userinput3 = input('SteamID32: ')
    SteamID_2_32_conv = (int(userinput3) - int(1)) // int(2)  # Calculate SteamID from SteamID32
    SteamID_2_64_conv = int(userinput3) + int(ID_change_value)  # Calculate SteamID64 from SteamID32
    print(pause)
    if (int(userinput3) % 2 == 0):  # EVEN
        Steam1 = int(SteamID_2_32_conv) + int(1)
        print('SteamID:   Steam_0:0:' + str(Steam1))  # print SteamID
        print('Steam3:    U:1:' + userinput3)  # Print Steam3
        print('SteamID32: ' + userinput3)  # Print SteamID32 (form user input)
        print('SteamID64: ' + str(SteamID_2_64_conv))  # Print SteamID64
        print(pause)
        # Save
        userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
        if userinputx == '1':
            file = open('history.txt', 'a')
            file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) + '\n' + 'Steam ID: Steam_0:0:' + str(
                Steam1) + '\n' + 'Steam3: U:1:' + (userinput3) + '\n' +
                       'Steam ID32: ' + (userinput3) + '\n' + 'Steam ID64: ' + str(SteamID_2_64_conv) +
                       '\n' + (pause))
            file.close()
            main_menu()
        else:
            main_menu()
    else:
        print('SteamID:   Steam_0:1:' + str(SteamID_2_32_conv))  # print SteamID
        print('Steam3:    U:1:' + userinput3)  # Print Steam3
        print('SteamID32: ' + userinput3)  # Print SteamID32 (form user input)
        print('SteamID64: ' + str(SteamID_2_64_conv))  # Print SteamID64
        print(pause)
        # Save
        userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
        if userinputx == '1':
            file = open('history.txt', 'a')
            file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) +
                       '\n' + 'Steam ID: Steam_0:1:' + str(SteamID_2_64_conv) + '\n' + 'Steam3: U:1:' + (
                       userinput3) + '\n' +
                       'Steam ID32: ' + (userinput3) + '\n' + 'Steam ID64: ' + str(SteamID_2_64_conv) +
                       '\n' + (pause))
            file.close()
            main_menu()
        else:
            main_menu()


def SteamID64_conv():  # 4
    print('Please Enter SteamID64 (XXXXXXXXXXXXXXXXX)')
    userinput4 = input('SteamID64: ')
    SteamID_2_64_conv = ((int(userinput4) - int(ID_change_value)) - int(1)) // int(
        2)  # Calculate SteamID from SteamID64
    SteamID32_64_conv = (int(userinput4) - int(ID_change_value))  # Calculate SteamID32 from SteamID64
    print(pause)
    if (int(userinput4) % 2 == 0):  # EVEN
        Steam2 = int(SteamID_2_64_conv) + int(1)
        print('SteamID:   Steam_0:0:' + str(Steam2))  # Print SteamID
        print('Steam3:    U:1:' + str(SteamID32_64_conv))  # Print Steam3
        print('SteamID32: ' + str(SteamID32_64_conv))  # Print SteamID32
        print('SteamID64: ' + userinput4)  # Print SteamID64 form user input
        print(pause)
        # Save
        userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
        if userinputx == '1':
            file = open('history.txt', 'a')
            file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) +
                       '\n' + 'Steam ID: Steam_0:0:' + str(Steam2) + '\n' + 'Steam3: U:1:' + str(
                SteamID32_64_conv) + '\n' +
                       'Steam ID32: ' + str(SteamID32_64_conv) + '\n' + 'Steam ID64: ' + (userinput4) +
                       '\n' + (pause))
            file.close()
            main_menu()
        else:
            main_menu()
    else:  # ODD
        print('SteamID:   Steam_0:1:' + str(SteamID_2_64_conv))  # Print SteamID
        print('Steam3:    U:1:' + str(SteamID32_64_conv))  # Print Steam3
        print('SteamID32: ' + str(SteamID32_64_conv))  # Print SteamID32
        print('SteamID64: ' + userinput4)  # Print SteamID64 form user input
        print(pause)
        userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
        if userinputx == '1':
            file = open('history.txt', 'a')
            file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) + '\n' + 'Steam ID: Steam_0:1:' + str(
                SteamID_2_64_conv) + '\n' + 'Steam3: U:1:' +
                       str(SteamID32_64_conv) + '\n' + 'Steam ID32: ' + str(SteamID32_64_conv) + '\n' +
                       'Steam ID64: ' + (userinput4) + '\n' + (pause))
            file.close()
            main_menu()
        else:
            main_menu()


ID_change_value = 76561197960265728
pause = ('----------------------------------------')
main_menu()
# By arhi3a
# More info about SteamID: (https://developer.valvesoftware.com/wiki/SteamID)
# ver. 1.0
