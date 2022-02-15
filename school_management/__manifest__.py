{
    'name': "School Management",
    'version': '1.0',
    'depends': ['base', 'sale','hr', 'purchase', 'mail','product','stock'],
    'author': "Arun George",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'wizard/popup_window_view.xml',
        'views/school_management_view.xml',
        'views/student_management_view.xml',
        'views/teacher_management_view.xml',
        'views/student_result_view.xml',
        'views/subject_list_view.xml',
        'views/school_tag_view.xml',
        'views/school_management_menu.xml',
        'views/employee_inherit_view.xml',
        'views/employee_inherit_add_field.xml',
        'views/purchase_info_view.xml',
        'views/purchase_sent_mail.xml',
        'reports/paper_format.xml',
        'reports/report.xml',
        'reports/student_report.xml',
        'reports/student_result.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,

}
