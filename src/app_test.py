import unittest
from tkinter import *
from unittest.mock import MagicMock
from tk import *

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.parent = Tk()
        self.client = None  
        self.id = None
        self.registration = Registration(self.parent, self.client, self.id)

    def tearDown(self):
        self.parent.destroy()

    def test_clear_search_pridumaytelogin(self):
        self.registration.pridumaytelogin.delete = MagicMock()
        self.registration.clear_search_pridumaytelogin(None)  
        self.registration.pridumaytelogin.delete.assert_called_once_with(0, END) 

    def test_clear_search_pridumayteparol(self):
        self.registration.pridumayteparol.delete = MagicMock()
        self.registration.clear_search_pridumayteparol(None)
        self.registration.pridumayteparol.delete.assert_called_once_with(0, END)

    def test_cont_failure_mismatch(self):
        self.registration.pridumaytelogin.get = MagicMock(return_value="testuser")
        self.registration.pridumayteparol.get = MagicMock(return_value="testpass")
        self.registration.povtoriteparol.get = MagicMock(return_value="wrongpass")
        self.registration.lbl1.place = MagicMock()
        self.registration.Cont()
        self.registration.lbl1.place.assert_called_once()
        

class TestProfil(unittest.TestCase):
    def setUp(self):
        self.parent = Tk()
        self.client = None
        self.id = None
        self.profil = Profil(self.parent, self.client, self.id)
        self.profil.name = MagicMock(spec=Entry)
        self.profil.surname = MagicMock(spec=Entry)
        self.profil.choice = MagicMock(spec=IntVar)
        self.profil.info = MagicMock()
        self.profil.top = MagicMock()
        self.profil.lbl1 = MagicMock()

    def tearDown(self):
        self.parent.destroy()

    def test_cont_valid_data(self):
        self.profil.name.get.return_value = "TestName"
        self.profil.surname.get.return_value = "TestSurname"
        self.profil.choice.set(1)
        self.assertTrue(self.profil.name.get() != '' and self.profil.name.get() != 'Enter your name' and self.profil.surname.get() != '' and self.profil.surname.get() != 'Enter your surname')

    def test_cont_invalid_data(self): 
        self.profil.name.get.return_value = ""
        self.profil.surname.get.return_value = ""
        self.profil.choice.set(0)
        self.assertFalse(self.profil.name.get() != '' and self.profil.name.get() != 'Enter your name' and self.profil.surname.get() != '' and self.profil.surname.get() != 'Enter your surname')

    def test_clear_search_name(self):
        self.profil.name.get.return_value = 'Enter your name'
        self.profil.clear_search_name(None)
        self.profil.name.delete.assert_called_once_with(0, END)

    def test_clear_search_surname(self):
        self.profil.surname.get.return_value = 'Enter your surname'
        self.profil.clear_search_surname(None)
        self.profil.surname.delete.assert_called_once_with(0, END)


class TestAnketa(unittest.TestCase):
    def test_anketa_creation(self):
        anketa = Anketa(None, None, None)
        self.assertIsNotNone(anketa) 

    def test_anketa_attributes(self):
        anketa = Anketa(None, None, None)
        self.assertIsNotNone(anketa.top1)
        self.assertIsNotNone(anketa.btn_start_search)
        self.assertIsNotNone(anketa.btnlike)
        self.assertIsNotNone(anketa.btndislike)
        self.assertIsNotNone(anketa.name)
        self.assertIsNotNone(anketa.surname)
        self.assertIsNotNone(anketa.gender)

    def test_button_attributes(self):
        anketa = Anketa(None, None, None)
        self.assertEqual(anketa.btn_start_search["text"], "Start search") 


if __name__ == '__main__':
    unittest.main()
