{
    'name': 'School Management',
    'version': '16.0.1.0.0',
    'summary': 'Manage Students, Teachers, Classes and Exams',
    'description': """
        School Management App
        ======================
        This module helps manage:
        - Students
        - Teachers
        - Classes
        - Attendance
        - Exams and Results
    """,
    'category': 'Education',
    'author': 'Naim Reza',
    'website': 'https://github.com/mdnaim346',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/course.xml',
         'views/student.xml',
        'views/teacher.xml',
        'views/menu.xml',
       
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
