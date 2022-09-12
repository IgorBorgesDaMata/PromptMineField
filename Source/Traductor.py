class Traductor:
    language = -1

    def GetLanguageInput(self):
        print(
            "Insira o numero da linguagem desejada (0 = ingles; 1 = portugues)"
        )
        print(
            "Insert the number of wished language (0 = english; 1 = portugues)"
        )
        languageInput = input()
        self.__SetLanguage(languageInput)

    def __SetLanguage(self, languageInput):
        insertedValidNumber = languageInput.isnumeric() and (
            int(languageInput) == 0 or int(languageInput) == 1)
        if insertedValidNumber:
            self.language = int(languageInput)
        else:
            print("\nInsira um nemero valido...")
            print("Insert a valid number...")
            self.GetLanguageInput()

    def GetText(self, enText, ptbrText):
        if self.language == 0:
            return enText
        return ptbrText