class Editor: 
    def __init__(self, filePath, chTemplate, chTemplateLen, difficultyIcon):
        self.FILE_PATH = filePath
        self.chTemplate = chTemplate
        self.chTemplatelen = int(chTemplateLen)
        self.difficultyIcon = difficultyIcon

    def info(self):
        info = """
        - Functions - 
        [ 1 ] f <flag> : 
        <-a> auto select the last line 
        <-s> editing specific linese

        """
        print(info)
    
    # Helper Functions
    def displayFile(self):
        if self.content:
            for line in self.content:
                print(line)
    
    # File Handling Functions
    def loadFile(self):
        with open(self.FILE_PATH, "r") as file:
            self.content = file.readlines()
    
    def updateFile(self):
        with open(self.FILE_PATH, "w") as file:
            file.writelines(self.content)
    
    # File Content Manipulation Functions
    def addHeading(self, line, text):
        heading = [f" {text} "]
        deco = ""
 
        # Generates Heading String
        while len(heading) < self.chTemplatelen:
            heading.insert(0, "_")
            heading.extend("_")
        headingString = "".join(heading)

        # Generates Decoration String
        for i in range(len(headingString)):
            deco += "_"

        self.content.insert(line, headingString)
        self.content.insert(line, "\n")
        self.content.insert(line, deco)

    def addSubHeading(self, line, text, difficulty):
        subheadingString = f"| {self.difficultyIcon * difficulty} {text} |"
        self.content.insert(line, subheadingString)

    def exec(self, args):
        if len(args) < 2: 
            self.info()
            exit()

        self.loadFile()

        # Mode
        if args[1][0] == "-": # Command Flag was specified
            mode = args[1][1]
        else: 
            mode = "s"
        
        line = int(input("Line: "))
        text = input("Input Text: ")
        response = input("Heading/Subheading [T/F]: ")
        match response:
            case 'T':
                self.addHeading(line - 1, text)
            
            case 'F':
                difficulty = int(input("Difficulty Level: "))
                self.addSubHeading(line - 1, text, difficulty)

        self.displayFile()
        self.updateFile()
        