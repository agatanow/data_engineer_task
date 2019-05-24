import unittest
from scripts.validator import Validator
from scripts.dataset_file import load_data, save_dataset
from scripts.test_utilization import get_test_utilization
from scripts.test_average_scores import get_test_average
from scripts.queries import TASK_3, TASK_4
from scripts.db_solution import EducationDataset
from audition_tasks import python_solution, sqlite_solution

class test_Validator(unittest.TestCase):

    def test_int_validator(self):
        test1 = {'this_is_int': 2, 'this_isnt_int': '2o', 'this_is_empty': ''}
        self.assertTrue(Validator.int_validator(dict(test1), 'this_is_int', False, not_null=True))
        self.assertTrue(Validator.int_validator(dict(test1), 'this_is_int', False, not_null=False))

        self.assertFalse(Validator.int_validator(dict(test1), 'this_isnt_int', False, not_null=True))
        self.assertFalse(Validator.int_validator(dict(test1), 'this_isnt_int', False, not_null=False))

        self.assertFalse(Validator.int_validator(dict(test1), 'this_is_empty', False, not_null=True))
        self.assertTrue(Validator.int_validator(dict(test1), 'this_is_empty', False, not_null=False))

    def test_float_validator(self):
        test1 = {'this_is_float': '2.73', 'this_isnt_float': '2ssss', 'this_is_empty': ''}
        self.assertTrue(Validator.float_validator(dict(test1), 'this_is_float', False, not_null=True))
        self.assertTrue(Validator.float_validator(dict(test1), 'this_is_float', False, not_null=False))

        self.assertFalse(Validator.float_validator(dict(test1), 'this_isnt_float', False, not_null=True))
        self.assertFalse(Validator.float_validator(dict(test1), 'this_isnt_float', False, not_null=False))

        self.assertFalse(Validator.float_validator(dict(test1), 'this_is_empty', False, not_null=True))
        self.assertTrue(Validator.float_validator(dict(test1), 'this_is_empty', False, not_null=False))

    def test_date_validator(self):
        date_format = '%d.%m.%y %H:%M'
        test1 = {'good_format': '05.05.19 20:22', 'wrong_format': '20:22 05.05.19', 'this_is_empty': ''}
        self.assertTrue(Validator.date_validator(dict(test1), 'good_format', date_format, False, not_null=False))
        self.assertTrue(Validator.date_validator(dict(test1), 'good_format', date_format, False, not_null=True))

        self.assertFalse(Validator.date_validator(dict(test1), 'wrong_format', date_format, False, not_null=True))
        self.assertFalse(Validator.date_validator(dict(test1), 'wrong_format', date_format, False, not_null=False))

        self.assertFalse(Validator.date_validator(dict(test1), 'this_is_empty', date_format, False, not_null=True))
        self.assertTrue(Validator.date_validator(dict(test1), 'this_is_empty', date_format, False, not_null=False))

    def test_isodate_validator(self):
        test1 = {'good_format': "2019-02-15T01:00:00+01:00", 'wrong_format': "2019.0.2.150T1:00:00+01:00", 'this_is_empty': ''}
        self.assertTrue(Validator.isodate_validator(dict(test1), 'good_format', False, not_null=False))
        self.assertTrue(Validator.isodate_validator(dict(test1), 'good_format', False, not_null=True))

        self.assertFalse(Validator.isodate_validator(dict(test1), 'wrong_format', False, not_null=True))
        self.assertFalse(Validator.isodate_validator(dict(test1), 'wrong_format', False, not_null=False))

        self.assertFalse(Validator.isodate_validator(dict(test1), 'this_is_empty', False, not_null=True))
        self.assertTrue(Validator.isodate_validator(dict(test1), 'this_is_empty', False, not_null=False))

    def test_validate_test(self):
        test1 = {
            'id': '12', 
            'student_id': '2',  
            'class_id': '3', 
            'created_at': '05.05.19 20:22', 
            'updated_at': '05.05.19 20:22',  
            'last_event_time': "2019-02-15T01:00:00+01:00", 
            'overall_score': '222',
            'authorized_at': '05.05.19 20:22',
            'confidence_level' : 'whatever',
            'speaking_score': '32',
            'writing_score': '322',
            'reading_score': '3222',
            'listening_score': '3222',
            'test_level_id':'6'
            }
        test2 = dict(test1)
        test2['id'] = 'asdf'
        self.assertTrue(Validator.validate_test(test1))
        self.assertFalse(Validator.validate_test(test2))

    def test_validate_test_level(self):
        test1 = {
            'id': '12', 
            'name': '2',  
            'displayName': '3', 
            'created_at': '05.05.19 20:22', 
            'updated_at': '05.05.19 20:22',  
            }
        test2 = dict(test1)
        test2['created_at'] = '05.05.19 20.22'
        self.assertTrue(Validator.validate_test_level(test1))
        self.assertFalse(Validator.validate_test_level(test2))

    def test_validate_class(self):
        test1 = {
            'id': '12', 
            'institution_id': '2',  
            'owner_id': '3', 
            'name': '3', 
            'created_at': '05.05.19 20:22', 
            'updated_at': '05.05.19 20:22', 
            'teaching_hours': '2222',
            'latest_test_time': '',
            'has_student_with_scored_test': '0'
            }
        test2 = dict(test1)
        test2['created_at'] = ''
        self.assertTrue(Validator.validate_class(test1))
        self.assertFalse(Validator.validate_class(test2))

unittest.main()
