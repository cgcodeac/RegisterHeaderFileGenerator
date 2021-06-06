

class DeviceRegister():
    '''Class for containing a register definition'''

    def __init__(self, name, description, numBits):
        self.name = name
        self.description = description
        self.numBits = numBits
        self.field = [] 

    def addField(self, name, description, startBitNum, numBits):
        self.field.append(RegisterField(name, description, startBitNum, numBits))

    # def rmField(self):

    def saveRegisterFile(self, filepath):
        with open(filepath, 'w') as fout:
            fout.write("R:Register Name:" + self.name + ":\n")
            fout.write("R:Register Description:" + self.description + ":\n")
            fout.write("R:Register numBits:" + str(self.numBits) + ":\n")

            fout.write("R:Num Fields:" + str(len(self.field))  + ':\n')
            for field in self.field:
                fout.write("    F:Name:" + field.name + ":\n")
                fout.write("    F:Description:" + field.description + ":\n")
                fout.write("    F:startBitNum:"    + str(field.startBitNum) + ":\n")
                fout.write("    F:numBits:"     + str(field.numBits) + ":\n")
                
                fout.write("    F:numSettings:" + str(len(field.setting)) + ':\n')
                for setting in field.setting:
                    fout.write("        S:Name:" + setting.name + ':\n')
                    fout.write("        S:Description:" + setting.description + ':\n')
                    fout.write("        S:Value:" + str(setting.value) + ':\n')
 
    def loadRegisterFile(self, filepath):
        with open(filepath) as fin:
            currLine = fin.readline()
            name = currLine.split(':')[2]
            currLine = fin.readline()
            description = currLine.split(':')[2]
            currLine = fin.readline()
            numBits = int(currLine.split(':')[2])
            self.__init__(name, description, numBits)

            currLine = fin.readline()
            numFields = int(currLine.split(':')[2])
            for i in range(0, numFields):
                currLine = fin.readline()
                name = currLine.split(':')[2]
                currLine = fin.readline()
                description = currLine.split(':')[2]
                currLine = fin.readline()
                startBitNum = int(currLine.split(':')[2])
                currLine = fin.readline()
                numBits = int(currLine.split(':')[2])
                self.addField(name, description, startBitNum, numBits)
 
                currLine = fin.readline()
                numSettings = int(currLine.split(':')[2])
                for j in range(0, numSettings):
                    currLine = fin.readline()
                    name = currLine.split(':')[2]
                    currLine = fin.readline()
                    description = currLine.split(':')[2]
                    currLine = fin.readline()
                    value = int(currLine.split(':')[2])
                    self.field[i].addSetting(name, description, value)

class RegisterField():
    '''A register field containing positions and group configurations '''
    def __init__(self, name, description, startBitNum, numBits):
        self.name = name
        self.description = description 
        self.startBitNum = startBitNum
        self.numBits     = numBits
        self.setting     = []  

    def addSetting(self, name, description, value):
        self.setting.append(FieldSetting(name, description, value))


class FieldSetting():
    '''Contains a name, value, and description of a setting for a register field'''

    def __init__(self, name, description, value):
        self.name = name
        self.value = value 
        self.description = description




# Register
#    - Name
#    - Description
#    - numBits
#    - Register Field
#           - Name
#           - Description
#           - Startbit
#           - numBits
#           - Settings
#               - name
#               - value
#               - description
