

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

#     def saveRegisterFile(self):

#     def loadRegisterFile(self):



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




# RegisterName
#    - Register Description
#    - Register Field
#           - Bit Range
#           - Description
#           - Group Configurations
