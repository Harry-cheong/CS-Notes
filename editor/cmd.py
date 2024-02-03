from datetime import datetime
from editor import Editor

class Command: 
    def __init__(self, binPath, config):
        self.BIN_PATH = binPath
        self.config = config
        self.f = Editor(self.config.getFilePath(), self.config.getchTemp(), self.config.getchTempLen(), self.config.getDifficultyIcon())
    
    def info(self):
        info = """
    <class> <executable> ...

        - CONFIG -
            [ 1 ] config path <filePath>
            [ 2 ] config chtemp <chapterTemplate>
            [ 3 ] config chtemplen <chapterTemplateLen>

        - EDITOR - 
            [ 1 ] f <flag> : 
            <-a> auto select the last line 
            <-s> editing specific lines
        """
        print(info)

    def exec(self, args):
        cmdClass = args[1]
        match cmdClass:
            case "config":
                self.config.exec(args[1:])
            
            case "f":
                self.f.exec(args[1:])
            
            case "help":
                self.info()
            
            case _:
                self.info()
        
                

        