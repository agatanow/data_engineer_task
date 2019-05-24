def get_test_utilization(tests, classes, test_levels):
    """Return test utilization dataset

    Keyword arguments:
    tests -- tests dataset
    classes -- classes dataset
    test_levels -- test_levels dataset
    show_all_classes -- if true the output dataset will contain all classes, even those that have
        no relation with authorized testor or any test in general.
    """
    res = {}
    class_counter = {}
    for test_id,test in tests.items():
        test_class = classes[test['class_id']]
        test_level = test_levels[test['test_level_id']]

        if test['authorized_at'] != '':
            #enumerate each solved test
            if test_class['id'] not in class_counter:
                class_counter[test_class['id']] = 0
            class_counter[test_class['id']] += 1

            #add test to output dataset
            res[test_id] = {
                'class_id': test_class['id'], 
                'class_name': test_class['name'],
                'teaching_hours': test_class['teaching_hours'],
                'test_id': test_id,
                'test_level': test_level['name'],
                'test_created_at': test['created_at'],
                'test_authorized_at': test['authorized_at'],
                'class_test_number': class_counter[test_class['id']]
            } 
    return res
