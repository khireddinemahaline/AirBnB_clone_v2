##!/usr/bin/python3
"""Test Amenity"""


import unittest
import models
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test Amenity"""
    def test_docstring(self):
        message = "modle doesn't hase docstring"
        self.assertIsNotNone(models.amenity.__doc__, message)
        message = "class doesn't has a docstring"
        self.assertIsNotNone(Amenity.__doc__, message)

    def test_excutable_file(self):
        is_read_true = os.access('models/amenity.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/amenity.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_excu_true = os.access('models/amenity.py', os.X_OK)
        self.assertTrue(is_excu_true)

    def test_init_Amenity(self):
        object = Amenity()
        self.assertIsInstance(object, Amenity)

    def test_id(self):
        object_id = Amenity()
        object_id1 = Amenity()
        self.assertNotEqual(object_id.id, object_id1.id)

    def test_str(self):
        object = Amenity()
        _dic = object.__dict__
        str1 = "[Amenity] ({}) {}".format(object.id, _dic)
        str2 = str(object)
        self.assertEqual(str1, str2)

    def test_save(self):
        objectup = Amenity()
        update_one = objectup.updated_at
        objectup.save()
        update_tow = objectup.updated_at
        self.assertNotEqual(update_one, update_tow)

    def test_to_dict(self):
        my_model3 = Amenity()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'Amenity':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
