#!/usr/bin/python3
"""test Review"""


import unittest
import models
import os
from models.review import Review


class TestReview(unittest.TestCase):
    """test review"""
    def test_docstring(self):
        message = "modle doesn't hase docstring"
        self.assertIsNotNone(models.review.__doc__, message)
        message = "class doesn't has a docstring"
        self.assertIsNotNone(Review.__doc__, message)

    def test_excutable_file(self):
        is_read_true = os.access('models/review.py', os.R_OK)
        self.assertTrue(is_read_true)
        is_write_true = os.access('models/review.py', os.W_OK)
        self.assertTrue(is_write_true)
        is_excu_true = os.access('models/review.py', os.X_OK)
        self.assertTrue(is_excu_true)

    def test_init_Review(self):
        object = Review()
        self.assertIsInstance(object, Review)

    def test_id(self):
        object_id = Review()
        object_id1 = Review()
        self.assertNotEqual(object_id.id, object_id1.id)

    def test_str(self):
        object = Review()
        _dic = object.__dict__
        str1 = "[Review] ({}) {}".format(object.id, _dic)
        str2 = str(object)
        self.assertEqual(str1, str2)

    def test_save(self):
        objectup = Review()
        update_one = objectup.updated_at
        objectup.save()
        update_tow = objectup.updated_at
        self.assertNotEqual(update_one, update_tow)

    def test_to_dict(self):
        my_model3 = Review()
        my_dict_model3 = my_model3.to_dict()
        self.assertIsInstance(my_dict_model3, dict)
        for key, value in my_dict_model3.items():
            flag = 0
            if my_dict_model3['__class__'] == 'Review':
                flag += 1
            self.assertTrue(flag == 1)
        for key, value in my_dict_model3.items():
            if key == 'created_at':
                self.assertIsInstance(value, str)
            if key == 'updated_at':
                self.assertIsInstance(value, str)


if __name__ == '__main__':
    unittest.main()
