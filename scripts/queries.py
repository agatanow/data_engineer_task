# Creates table for classes
CREATE_CLASS_TABLE = (
    'CREATE TABLE CLASS ('
        'id INTEGER PRIMARY KEY, '
        'institution_id INTEGER NOT NULL, '
        'owner_id VARCHAR(30), '
        'name VARCHAR(50),'
        'created_at DATE NOT NULL, '
        'updated_at DATE, '
        'teaching_hours VARCHAR(10), '
        'latest_test_time VARCHAR(30),'
        'has_student_with_scored_test VARCHAR(10));')

# Creates table for tests' levels
CREATE_TEST_LEVEL_TABLE = (
    'CREATE TABLE TEST_LEVEL ('
        'id INTEGER PRIMARY KEY, '
        'name VARCHAR(10), ' 
        'displayName VARCHAR(10), '
        'created_at DATE NOT NULL, '
        'updated_at DATE); ')

# Creates table for tests
CREATE_TEST_TABLE = (
    'CREATE TABLE TEST ( '
        'id INTEGER PRIMARY KEY, '
        'student_id INTEGER NOT NULL, '
        'class_id INTEGER NOT NULL, '
        'created_at DATE NOT NULL, '
        'updated_at DATE, '
        'last_event_time DATE, '
        'overall_score FLOAT, '
        'test_status VARCHAR(30), '
        'institution_id VARCHAR(10), '
        'authorized_at DATE, '
        'confidence_level, '
        'speaking_score FLOAT, '
        'writing_score FLOAT, '
        'reading_score FLOAT, '
        'listening_score FLOAT, '
        'test_level_id INTEGER NOT NULL, '
        'licence_id INTEGER, '
        'FOREIGN KEY(class_id) REFERENCES CLASS(id), '
        'FOREIGN KEY(test_level_id) REFERENCES TEST_LEVEL(id)); ')

# Creates test_utilization table in database
TASK_3 = (
    'CREATE TABLE TEST_UT AS '
    'SELECT '
    't.class_id AS class_id, '
    'c.name AS class_name, '
    'c.teaching_hours, '
    't.id AS test_id, '
    't.created_at AS test_created_at, '
    't.authorized_at AS test_authorized_at, '
    'tl.name AS test_level, '
    '(SELECT COUNT(*) FROM TEST t2 WHERE t2.authorized_at != "" AND t2.id <= t.id AND t2.class_id = t.class_id) AS class_test_number '
    'FROM TEST t '
    'JOIN CLASS c ON t.class_id = c.id '
    'JOIN TEST_LEVEL tl ON t.test_level_id = tl.id '
    'WHERE t.authorized_at != ""'
    'ORDER BY t.id;')

# Creates test_average_scores table in database
TASK_4 = (
    'CREATE TABLE TEST_AVG AS '
    'SELECT '
    't.class_id, '
    'c.name AS class_name, '
    'c.teaching_hours, '
    't.created_at AS test_created_at, '
    't.authorized_at AS test_authorized_at, '
    'AVG(t.overall_score) as avg_class_test_overall_score '
    'FROM TEST t '
    'JOIN CLASS c ON t.class_id = c.id '
    'WHERE t.authorized_at != "" AND t.test_status = "SCORING_SCORED" '
    'GROUP BY t.class_id;')
    