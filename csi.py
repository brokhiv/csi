import os
import json

class UserData:
    def __init__(self):
        self.data = {}

    def load_user_data(self, file_path):
        current_dir = os.getcwd()
        print(current_dir)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                self.data = json.load(file)
        else:
            print("Initializing user data file...")
            self.data = {
                "RoyF": ("groteZaken", False),
                "EtienneH": ("heleGroteZaken", False),
                "MartijnA": ("JessesFiets", False)
            }
            self.save_user_data(file_path)
            print("Finished Loading")

    def save_user_data(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.data, file)

    def authenticate_user(self, username, password):
        if username in self.data and not self.data[username][1]:
            stored_password, used = self.data[username]
            if password == stored_password:
                self.data[username] = (stored_password, True)
                return True
        return False

def report():
    print("Selecteer rapport (typ rapportnummer):")
    print("(1) Sectie Slachtoffer")
    print("(2) Inspectie Plaats Delict")
    print("(3) Sporenonderzoek op De Hei")
    input_nr = input()
    if input_nr == "1":
        print("Het slachtoffer is vermoedelijk overleden aan een klap op haar achterhoofd, waarschijnlijk als gevolg van een val. Ook is aan de voorkant van haar hoofd een wond gevonden die qua vorm op een sleutel lijkt.")
    elif input_nr == "2":
        print("Bij het lichaam is een zaklamp aangetroffen, met daarop de vingerafdrukken van het slachtoffer. Ook lijkt deze zaklamp recent gebruikt te zijn geweest door het slachtoffer.")
    elif input_nr == "3":
        print("In en om de gehele blokhut zijn sporen gevonden van alle betrokkenen. Het meest opvallend was echter dat er bloedspetters van het slachtoffer zijn aangetroffen tussen de blokhut en het bijgebouw.")

def main():
    user_data_file = "user_data.json"
    user_data_manager = UserData()

    user_data_manager.load_user_data(user_data_file)

    username = input("Gebruikersnaam: ")
    password = input("Wachtwoord: ")

    authenticated = user_data_manager.authenticate_user(username, password)

    if authenticated:
        print("Gebruiker succesvol ingelogd.")
        # Add your program logic here
        report()
        # Update user data after program use
        user_data_manager.save_user_data(user_data_file)
        print("KRITIEK: DATALEK GEDETECTEERD. Gebruiker uitgelogd en verwijderd.")
    else:
        print("Fout: gebruiker niet gevonden of onjuist wachtwoord.")

if __name__ == "__main__":
    main()
    while True:
        pass
