from datetime import datetime
import dateutil.parser

class Validator(object):
    @staticmethod
    def int_validator(x, name, show_incorrect, not_null=True):
        try:
            if not_null or x[name] != '':
                x[name] = int(x[name]) 
        except ValueError:
            if show_incorrect:
                print('Test field "{}" has incorrect format {} (expected int)'.format(name,x[name]))
            return False
        return True
    
    @staticmethod
    def float_validator(x, name, show_incorrect, not_null=True):
        try:
            if not_null or x[name] != '':
                x[name] = float(x[name]) 
        except ValueError:
            if show_incorrect:
                print('Test field "{}" has incorrect format {} (expected float)'.format(name,x[name]))
            return False
        return True
    
    @staticmethod
    def date_validator(x, name, date_format, show_incorrect, not_null=True):
        try:
            if not_null or x[name] != '':
                x[name] = datetime.strptime(x[name], date_format) 
        except ValueError:
            if show_incorrect:
                print('Test field "{}" has incorrect format {} (expected date format: {})'.format(name,x[name], date_format))
            return False
        return True
    
    @staticmethod
    def isodate_validator(x, name, show_incorrect, not_null=True):
        try:
            if not_null or x[name] != '':
                x[name] = dateutil.parser.parse(x[name])
        except ValueError:
            if show_incorrect:
                print('Test field "{}" has incorrect format {} (expected isodate format)'.format(name,x[name], date_format))
            return False
        return True
    
    @staticmethod
    def validate_test(row, show_incorrect=False):
        return ( Validator.int_validator(row, 'id', show_incorrect) and
            Validator.int_validator(row, 'student_id', show_incorrect) and
            Validator.int_validator(row, 'class_id', show_incorrect) and
            Validator.date_validator(row, 'created_at', '%d.%m.%y %H:%M', show_incorrect) and
            Validator.date_validator(row, 'updated_at', '%d.%m.%y %H:%M', show_incorrect, not_null=False) and
            Validator.isodate_validator(row, 'last_event_time', show_incorrect, not_null=False) and
            Validator.float_validator(row, 'overall_score', show_incorrect, not_null=False) and
            Validator.date_validator(row, 'authorized_at', '%d.%m.%y %H:%M', show_incorrect,not_null=False) and
            Validator.float_validator(row, 'speaking_score', show_incorrect, not_null=False) and
            Validator.float_validator(row, 'writing_score', show_incorrect, not_null=False) and
            Validator.float_validator(row, 'reading_score', show_incorrect, not_null=False) and
            Validator.float_validator(row, 'listening_score', show_incorrect, not_null=False) and
            Validator.int_validator(row, 'test_level_id', show_incorrect))
    
    @staticmethod
    def validate_class(row, show_incorrect=False):
        return ( Validator.int_validator(row, 'id', show_incorrect) and
            Validator.int_validator(row, 'institution_id', show_incorrect, not_null=False) and
            Validator.date_validator(row, 'created_at', '%d.%m.%y %H:%M', show_incorrect) and
            Validator.date_validator(row, 'updated_at', '%d.%m.%y %H:%M', show_incorrect, not_null=False))
    
    @staticmethod
    def validate_test_level(row, show_incorrect=False):
        return ( Validator.int_validator(row, 'id', show_incorrect) and
            Validator.date_validator(row, 'created_at', '%d.%m.%y %H:%M', show_incorrect) and
            Validator.date_validator(row, 'updated_at', '%d.%m.%y %H:%M', show_incorrect, not_null=False))
    
