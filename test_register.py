from register import DeviceRegister
import unittest


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
        self.assertEqual(statusReg.field[0].setting[0].name, "WDTExpired") 
        self.assertEqual(statusReg.field[0].setting[0].description, "The watchdog timer expired") 
        self.assertEqual(statusReg.field[0].setting[0].value, 1) 





