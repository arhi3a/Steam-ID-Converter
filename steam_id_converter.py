class Convert(object):
    """Class for converting SteamID between different versions of it"""

    def __init__(self, steamid):
        """Init"""
        self.sid = steamid
        self.change_val = 76561197960265728
        self.alert()

    def set_steam_id(self, steamid):
        """Sets new steam ID"""
        self.sid = steamid
        self.recognize_sid()
        self.alert()

    def get_steam_id(self):
        """Returns given Steam ID"""
        return self.sid

    def recognize_sid(self, choice=0):
        """Recognized inputted steamID
        SteamID code = 1
        SteamID3 code = 2
        SteamID32 code = 3
        SteamID64 code = 4
        Not found = 0
        Choice int 1 or 0
        1- prints recognized steam ID and returns code
        0- Returns only code"""
        if choice is not 0 and choice is not 1:
            print('Assuming choice is 1')
            choice = 1
        if self.sid[0] == 'S':  # SteamID
            if choice == 1:
                print('Recognized ', self.sid, ' as SteamID')
            return 1
        elif self.sid[0] in ['U', 'I', 'M', 'G', 'A', 'P', 'C', 'g', 'T', 'L', 'C', 'a']:  # SteamID3
            if choice == 1:
                print('Recognized ', self.sid, ' as SteamID3')
            return 2
        elif self.sid[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and len(self.sid) < 17:  # SteamID32
            if choice == 1:
                print('Recognized ', self.sid, ' as SteamID32')
            return 3
        elif self.sid[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and len(self.sid) == 17:  # SteamID64
            if choice == 1:
                print('Recognized ', self.sid, ' as SteamID64')
            return 4
        else:
            if choice == 1:
                print(self.sid, 'is not recognized as any SteamID')
            return 0

    def alert(self):
        """Prints alert when user tries to convert one of special accounts"""
        recognized = self.recognize_sid(0)
        if recognized == 1:
            if self.sid[6] != '0':
                print('Result of converting:', self.sid, 'steam ID may not be correct')
        elif recognized == 2:
            if self.sid[0] != 'U':
                print('Result of converting:', self.sid, 'steam ID may not be correct')

    def steam_id_converter(self):
        """Converts other SteamID versions to steamID"""
        recognized = self.recognize_sid(0)
        if recognized == 1:  # Returns steamID
            return self.sid
        elif recognized == 2:  # Converts SteamID3 to SteamID
            steam3 = int(self.sid[4:])
            return 'STEAM_0:' + str(self.oddity(steam3)) + ':' + str(steam3 // 2)
        elif recognized == 3:  # Converts SteamID32 to SteamID
            steam3 = int(self.sid)
            return 'STEAM_0:' + str(self.oddity(steam3)) + ':' + str(steam3 // 2)
        elif recognized == 4:  # Converts SteamID64 SteamID64
            steam3 = int(self.steam_id32_converter())
            return 'STEAM_0:' + str(self.oddity(steam3)) + ':' + str(steam3 // 2)

    @staticmethod
    def oddity(number):
        """Checks oddity of given number"""
        if number % 2 == 0:
            return 0
        else:
            return 1

    def steam_id3_converter(self):
        """Converts other SteamID versions to SteamID3"""
        recognized = self.recognize_sid(0)
        if recognized == 1:  # Converts SteamID to SteamID3
            return 'U:1:' + str(self.steam_id32_converter())
        elif recognized == 2:  # returns SteamID3
            return self.sid
        elif recognized == 3:  # Converts SteamID32 to SteamID3
            return 'U:1:' + str(self.sid)
        elif recognized == 4:  # Converts SteamID64 to SteamID3
            return 'U:1:' + str(int(self.sid) - self.change_val)

    def steam_id32_converter(self):
        """Converts other steamID versions to steamID32"""
        recognized = self.recognize_sid(0)
        if recognized == 1:  # Converts from steamID to SteamID32
            y = self.sid[8:9]  # STEAM_0:y:zzzzzz
            z = self.sid[10:]  # STEAM_0:y:zzzzzz
            return int(z) * int(2) + int(y)
        elif recognized == 2:  # Converts from steamID3 to SteamID32
            return int(self.sid[4:])
        elif recognized == 3:  # Returns steamID32
            return int(self.sid)
        elif recognized == 4:  # Converts from steamID64 to SteamID32
            return int(self.sid) - self.change_val

    def steam_id64_converter(self):
        """Converts other SteamID versions to SteamID64"""
        recognized = self.recognize_sid(0)
        if recognized == 1:  # Converts from steamID to SteamID64
            y = self.sid[8:9]  # STEAM_0:y:zzzzzz
            z = self.sid[10:]  # STEAM_0:y:zzzzzz
            return int(z) * int(2) + int(y) + self.change_val
        elif recognized == 2:  # Converts steamID3 to SteamID64
            return int(self.sid[4:]) + self.change_val
        elif recognized == 3:  # Converts steamID32 to SteamID64
            return int(self.sid) + self.change_val
        elif recognized == 4:  # Returns steamID64
            return int(self.sid)


class Menu(Convert):
    """Simple text menu for converter"""

    def __init__(self, steam_id):
        """init"""
        self.steam_id = steam_id
        self.convert_all()
        Menu.options()

    @classmethod
    def options(cls):
        """Asks for user input"""
        return cls(
            input('Enter Steam ID: ')
        )

    def get_input(self):
        """Returns user input"""
        return self.steam_id

    def convert_all(self):
        """Converts to all steamID versions"""
        steamid = Convert(self.steam_id).steam_id_converter()
        steamid3 = Convert(self.steam_id).steam_id3_converter()
        steamid32 = Convert(self.steam_id).steam_id32_converter()
        steamid64 = Convert(self.steam_id).steam_id64_converter()
        print('SteamID:  ', steamid)
        print('SteamID3: ', steamid3)
        print('SteamID32:', steamid32)
        print('SteamID64:', steamid64)


a = Menu.options()

# By arhi3a
# More info about SteamID: (https://developer.valvesoftware.com/wiki/SteamID)
# ver. 2.0
