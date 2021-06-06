from register import DeviceRegister
import unittest
import filecmp


class RegisterClassTests(unittest.TestCase):

    def test_create_register_class_init(self):
        statusReg = DeviceRegister("STATUS", "Provides Status Info", 8)
        self.assertEqual(statusReg.name, "STATUS")
        self.assertEqual(statusReg.description, "Provides Status Info")
        self.assertEqual(statusReg.numBits, 8)


    def test_addField(self):
        statusReg = DeviceRegister("STATUS", "Provides Status Info",8)
        statusReg.addField("nTO", "Time Out Bit", 2, 3)
        self.assertEqual(statusReg.field[0].name, "nTO")
        self.assertEqual(statusReg.field[0].description, "Time Out Bit")
        self.assertEqual(statusReg.field[0].startBitNum, 2)
        self.assertEqual(statusReg.field[0].numBits,     3)


    def test_addFieldSetting(self): 
        statusReg = DeviceRegister("STATUS", "Provides Status Info", 8)
        statusReg.addField("nTO", "Time Out Bit", 2, 3)
        statusReg.field[0].addSetting("WDTExpired", "The watchdog timer expired", 1)
        statusReg.field[0].addSetting("WDTCleared", "The watchdog time has not expired", 0)
        self.assertEqual(statusReg.field[0].setting[0].name, "WDTExpired") 
        self.assertEqual(statusReg.field[0].setting[0].description, "The watchdog timer expired") 
        self.assertEqual(statusReg.field[0].setting[0].value, 1) 



    def test_saveRegisterFile(self): 
        statusReg = DeviceRegister("STATUS", "Provides Status Info", 8)
        statusReg.addField("nTO", "Time Out Bit", 2, 3)
        statusReg.field[0].addSetting("WDTExpired", "The watchdog timer expired", 1)
        statusReg.field[0].addSetting("WDTCleared", "The watchdog time has not expired", 0)
        statusReg.saveRegisterFile("./test_StatusRegTestSave.txt")

    
    def test_loadSaveRegisterFile(self): 
        statusReg = DeviceRegister("", "", 0)
        statusReg.loadRegisterFile("./test_StatusRegTestSave.txt")
        statusReg.saveRegisterFile("./test_StatusRegTestLoad.txt")
        identical = filecmp.cmp("./test_StatusRegTestSave.txt", "./test_StatusRegTestLoad.txt")
        self.assertEqual(identical, True)

