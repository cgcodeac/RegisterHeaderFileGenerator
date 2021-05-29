from register import DeviceRegister
import unittest


class RegisterClassTests(unittest.TestCase):

    def test_create_register_class_init(self):
        statusReg = DeviceRegister("STATUS", "Provides Status Info")
        self.assertEqual(statusReg.name, "STATUS")
        self.assertEqual(statusReg.description, "Provides Status Info")


    def test_addField(self):
        statusReg = DeviceRegister("STATUS", "Provides Status Info")
        statusReg.addField("nTO", "Time Out Bit")
        self.assertEqual(statusReg.field[0].name, "nTO")
        self.assertEqual(statusReg.field[0].description, "Time Out Bit")





