from scripts.validator import Validator
from scripts.dataset_file import load_data, save_dataset
from scripts.test_utilization import get_test_utilization
from scripts.test_average_scores import get_test_average
from scripts.queries import TASK_3, TASK_4
from scripts.db_solution import EducationDataset


def python_solution():
    """solve all tasks using Python"""
    tests = load_data('input_data/test.csv', Validator.validate_test)
    classes = load_data('input_data/class.csv', Validator.validate_class)
    test_levels = load_data('input_data/test_level.csv', Validator.validate_test_level)
    tests_ut = get_test_utilization(tests, classes, test_levels)
    tests_av = get_test_average(tests_ut, tests, classes)

    fieldnames_ut = [ 'class_id', 'class_name', 'teaching_hours', 'test_id',
                    'test_created_at', 'test_authorized_at', 'test_level', 'class_test_number']

    fieldnames_av = ['class_id', 'class_name', 'teaching_hours', 'test_created_at',
                            'test_authorized_at', 'avg_class_test_overall_score']

    save_dataset(tests_ut, 'results/test_utilization.csv', fieldnames_ut)  
    save_dataset(tests_av, 'results/test_average_scores.csv', fieldnames_av)

def sqlite_solution():
    """solve all tasks using sqlite3 in Python"""
    ed = EducationDataset("ed", 'input_data/test.csv', 'input_data/class.csv', 'input_data/test_level.csv')
    ed.do_task(TASK_3, 8)
    ed.do_task(TASK_4, 6)

if __name__ == "__main__":
    python_solution()
    sqlite_solution()