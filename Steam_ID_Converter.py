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
        steamid32_conv()
    elif userinput1 == '4':  # Enter SteamID64
        steam_id64_conv()
    else:
        print('Wrong number returning')
        main_menu()


def SteamID_conv():  # 1
    print('Please Enter SteamID (Steam_x:x:xxxxxxxx)')
    userinput2 = input('SteamID:  ')
    y = userinput2[8:9]  # STEAM_0:y:zzzzzz
    z = userinput2[10:]  # STEAM_0:y:zzzzzz
    steamid_to_32 = int(z) * int(2) + int(y)  # Calculate steamID32
    steamid_to_64 = int(steamid_to_32) + int(ID_change_value)  # Calculate SteamID64 from steamID32
    steamid3 = 'U:1:' + str(steamid_to_32)  # Calculate SteamID3 from input and ID32
    print(pause)
    print('Steam ID:   ', userinput2)  # Print steamID from user input
    print('Steam ID3:  ', steamid3)  # Print SteamID3
    print('Steam ID32: ', steamid_to_32)  # Print SteamID32
    print('Steam ID64: ', steamid_to_64)  # Print SteamID64
    print(pause)
    # Save
    userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
    if userinputx == '1':
        file = open('history.txt', 'a')
        file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) + '\n' + 'Steam ID: ' + (
            userinput2) + '\n' + 'Steam ID3: ' + (steamid3) + '\n' +
                   'Steam ID32: ' + str(steamid_to_32) + '\n' + 'Steam ID64: ' + str(steamid_to_64) + '\n' + (
                       pause))
        file.close()
        main_menu()
    else:
        main_menu()


def Steam3_conv():  # 2
    print('Please Enter Steam3: (U:X:XXXXXXXX)')
    userinput5 = input('Steam3: ')
    steam3_to_32 = (int(userinput5[4:]))
    steam3_to_64 = int(steam3_to_32) + int(ID_change_value)
    steam3_to_steamid = int(steam3_to_32) // int(2)
    print(pause)
    if (int(steam3_to_64) % 2 == 0):  # Even
        print('SteamID:   Steam_0:0:' + str(steam3_to_steamid))  # Print SteamID
        print('Steam3:    ' + userinput5)  # Print Steam3 from userinput
        print('SteamID32: ' + str(steam3_to_32))  # Print SteamID32
        print('SteamID64: ' + str(steam3_to_64))  # Print SteamID64 form user input
        print(pause)
        # Save
        userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
        if userinputx == '1':
            file = open('history.txt', 'a')
            file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) +
                       '\n' + 'Steam ID: Steam_0:0:' + str(steam3_to_steamid) + '\n' + 'Steam ID3: ' + (
                           userinput5) + '\n' +
                       'Steam ID32: ' + str(steam3_to_32) + '\n' + 'Steam ID64: ' + str(steam3_to_64) +
                       '\n' + (pause))
            file.close()
            main_menu()
        else:
            main_menu()
    else:  # Odd
        print('SteamID:   Steam_0:1:' + str(steam3_to_steamid))  # Print SteamID
        print('Steam3:    ' + userinput5)  # Print Steam3 from userinput
        print('SteamID32: ' + str(steam3_to_32))  # Print SteamID32
        print('SteamID64: ' + str(steam3_to_64))  # Print SteamID64 form user input
        print(pause)
        # Save
        userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
        if userinputx == '1':
            file = open('history.txt', 'a')
            file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) +
                       '\n' + 'Steam ID: Steam_0:1:' + str(steam3_to_steamid) + '\n' + 'Steam ID3: ' + (
                           userinput5) + '\n' +
                       'Steam ID32: ' + str(steam3_to_32) + '\n' + 'Steam ID64: ' + str(steam3_to_64) +
                       '\n' + (pause))
            file.close()
            main_menu()
        else:
            main_menu()


def steamid32_conv():  # 3
    print('Please Enter SteamID32 (XXXXXXXX)')
    userinput3 = input('SteamID32: ')
    steam32_to_steamid = (int(userinput3) - int(1)) // int(2)  # Calculate SteamID from SteamID32
    steam32_to_64 = int(userinput3) + int(ID_change_value)  # Calculate SteamID64 from SteamID32
    print(pause)
    if (int(userinput3) % 2 == 0):  # EVEN
        steam1 = int(steam32_to_steamid) + int(1)
        print('SteamID:   Steam_0:0:' + str(steam1))  # print SteamID
        print('Steam3:    U:1:' + userinput3)  # Print Steam3
        print('SteamID32: ' + userinput3)  # Print SteamID32 (form user input)
        print('SteamID64: ' + str(steam32_to_64))  # Print SteamID64
        print(pause)
        # Save
        userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
        if userinputx == '1':
            file = open('history.txt', 'a')
            file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) + '\n' + 'Steam ID: Steam_0:0:' + str(
                steam1) + '\n' + 'Steam3: U:1:' + (userinput3) + '\n' +
                       'Steam ID32: ' + (userinput3) + '\n' + 'Steam ID64: ' + str(steam32_to_64) +
                       '\n' + (pause))
            file.close()
            main_menu()
        else:
            main_menu()
    else:
        print('SteamID:   Steam_0:1:' + str(steam32_to_steamid))  # print SteamID
        print('Steam3:    U:1:' + userinput3)  # Print Steam3
        print('SteamID32: ' + userinput3)  # Print SteamID32 (form user input)
        print('SteamID64: ' + str(steam32_to_64))  # Print SteamID64
        print(pause)
        # Save
        userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
        if userinputx == '1':
            file = open('history.txt', 'a')
            file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) +
                       '\n' + 'Steam ID: Steam_0:1:' + str(steam32_to_64) + '\n' + 'Steam3: U:1:' + (
                           userinput3) + '\n' +
                       'Steam ID32: ' + (userinput3) + '\n' + 'Steam ID64: ' + str(steam32_to_64) +
                       '\n' + (pause))
            file.close()
            main_menu()
        else:
            main_menu()


def steam_id64_conv():  # 4
    print('Please Enter SteamID64 (XXXXXXXXXXXXXXXXX)')
    userinput4 = input('SteamID64: ')
    steamid64_to_steamid = ((int(userinput4) - int(ID_change_value)) - int(1)) // int(
        2)  # Calculate SteamID from SteamID64
    steam64_to_steam32 = (int(userinput4) - int(ID_change_value))  # Calculate SteamID32 from SteamID64
    print(pause)
    if (int(userinput4) % 2 == 0):  # EVEN
        steam2 = int(steamid64_to_steamid) + int(1)
        print('SteamID:   Steam_0:0:' + str(steam2))  # Print SteamID
        print('Steam3:    U:1:' + str(steam64_to_steam32))  # Print Steam3
        print('SteamID32: ' + str(steam64_to_steam32))  # Print SteamID32
        print('SteamID64: ' + userinput4)  # Print SteamID64 form user input
        print(pause)
        # Save
        userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
        if userinputx == '1':
            file = open('history.txt', 'a')
            file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) +
                       '\n' + 'Steam ID: Steam_0:0:' + str(steam2) + '\n' + 'Steam3: U:1:' + str(
                steam64_to_steam32) + '\n' +
                       'Steam ID32: ' + str(steam64_to_steam32) + '\n' + 'Steam ID64: ' + (userinput4) +
                       '\n' + (pause))
            file.close()
            main_menu()
        else:
            main_menu()
    else:  # ODD
        print('SteamID:   Steam_0:1:' + str(steamid64_to_steamid))  # Print SteamID
        print('Steam3:    U:1:' + str(steam64_to_steam32))  # Print Steam3
        print('SteamID32: ' + str(steam64_to_steam32))  # Print SteamID32
        print('SteamID64: ' + userinput4)  # Print SteamID64 form user input
        print(pause)
        userinputx = input('Do you want to save this SteamID to history?' '\n' '1. Yes' '\n' '2. No' '\n' 'Answer: ')
        if userinputx == '1':
            file = open('history.txt', 'a')
            file.write('\n' + (strftime("%a, %d %b %Y %H:%M:%S ", localtime())) + '\n' + 'Steam ID: Steam_0:1:' + str(
                steamid64_to_steamid) + '\n' + 'Steam3: U:1:' +
                       str(steam64_to_steam32) + '\n' + 'Steam ID32: ' + str(steam64_to_steam32) + '\n' +
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
