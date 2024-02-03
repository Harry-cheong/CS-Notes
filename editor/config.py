import configparser
import os

class Config: 
    CONFIG_PATH = '../config.ini'

    def __init__(self):
        self.config = configparser.ConfigParser()

        if not os.path.exists(self.CONFIG_PATH):
            f = open(self.CONFIG_PATH, "x", encoding="utf-8")

            self.config['SETTINGS'] = {'FilePath': '\\', 'ChapterTemplate': '_', 'ChapterTemplateLength': 50, 'DifficultyIcon': "[ 🌟 ]"}

            with open(self.CONFIG_PATH, 'w', encoding="utf-8") as configFile:
                self.config.write(configFile)
        else:
            self.config.read(self.CONFIG_PATH)

            # Loading configs

            self.FILE_PATH = self.config['SETTINGS']['FilePath']
            if os.path.exists(self.FILE_PATH):
                print(f"File located at \"{self.FILE_PATH}\"\n")
            else:
                print("No Set File Path\n")

            self.chTemp = self.config['SETTINGS']['ChapterTemplate']
            self.chTempLen = self.config['SETTINGS']['ChapterTemplateLength']
            self.difficultyIcon = self.config['SETTINGS']['DifficultyIcon']

    # Error Catching
    def info(self):
        info = """
        - Config Functions - 
        [ 1 ] config path <filePath>
        [ 2 ] config chtemp <chapterTemplate>
        [ 3 ] config chtemplen <chapterTemplateLen>
        """
        print(info)

    # Helper Functions
    def getFilePath(self):
        return self.FILE_PATH
    
    def getchTemp(self):
        return self.chTemp
    
    def getchTempLen(self):
        return self.chTempLen

    def getDifficultyIcon(self):
        return self.difficultyIcon
    
    def addFilePath(self, filePath):
        if os.path.exists(filePath):
            self.FILE_PATH = self.config['SETTINGS']['FilePath'] = filePath
            print(f"Registered File Path {self.FILE_PATH}")
        else: 
            print(f"File at\"{filePath}\" not found \n")

    def addchTemp(self, chTemp):
        self.chTemp = self.config['SETTINGS']['ChapterTemplate'] = chTemp

    def addchTempLen(self, chTempLen):
        self.chTempLen = self.config['SETTINGS']['ChapterTemplateLength'] =  chTempLen
    
    # Exec Functions
    def exec(self, args): 
        match args[1]:
            case "path":
                self.addFilePath(" ".join(args[2:]))
            
            case _:
                self.info()
        self.updateFile()

    def updateFile(self):
        with open(self.CONFIG_PATH, 'w') as configFile: 
            self.config.write(configFile)
    