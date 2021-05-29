

class DeviceRegister():
    '''Class for containing a register definition'''

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.field = [] 

    def addField(self, name, description):
        self.field.append(RegisterField(name, description))

#     def rmField(self):

#     def saveRegisterFile(self):

#     def loadRegisterFile(self):



class RegisterField():
    '''A register field containing positions and group configurations '''
    def __init__(self, name, description):
        self.name = name
        self.description = description 
        # self.
        # self.groupconfigs = []



# RegisterName
#    - Register Description
#    - Register Field
#           - Bit Range
#           - Description
#           - Group Configurations
