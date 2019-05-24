def dict_filter(org_dic, *list_el):
    """Return dictonary like org_dic with removed elements from list_el"""
    dic = dict(org_dic)
    for x in list_el:
        dic.pop(x)
    return dic
        

def get_test_average(tests_ut, tests, classes, show_all_classes = False):
    """Return test average overall scores dataset

    Keyword arguments:
    tests_ut -- test utilization dataset
    tests -- tests dataset
    classes -- classes dataset
    show_all_classes -- if true the output dataset will contain all classes, even those that have
        no relation with authorized test or any test in general.
    """
    res = {}
    class_counter = {}

    for test_id, test_ut in tests_ut.items():
        test_status = tests[test_id]['test_status']
        test_score = tests[test_id]['overall_score']
        new_class = dict_filter(test_ut, 'test_level', 'test_id', 'class_test_number')

        #add new class to output dataset
        if test_ut['class_id'] not in res:
            res[test_ut['class_id']] = new_class

        #if test has a score and its status is 'SCORING_SCORED' use it for computing the average score
        if test_status == 'SCORING_SCORED' and test_score!='':
            if 'avg_class_test_overall_score' in res[test_ut['class_id']]:
                res[test_ut['class_id']]['avg_class_test_overall_score'] += float(test_score)
                class_counter[test_ut['class_id']] += 1
            else:
                res[test_ut['class_id']]['avg_class_test_overall_score'] = float(test_score)
                class_counter[test_ut['class_id']] = 1

    #compute average score from scores sum and tests number
    for class_id, class_res in res.items():
            if 'avg_class_test_overall_score' in class_res:
                class_res['avg_class_test_overall_score'] /= class_counter[class_id]
                
    #add every class from classes to ouput dataset (with empty fields)
    if show_all_classes:
        for class_id, cl in classes.items():
            if class_id not in res:
                res[class_id] = {
                    'class_id': class_id,
                    'class_name': cl['name'],
                    'teaching_hours': cl['teaching_hours']
                }
    return res

