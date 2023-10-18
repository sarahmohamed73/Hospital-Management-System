{
    "name":"Hospital Management System",
    "author":"sarah",
    'depends': ['base','crm'],
    "data": [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/hms_patient_views.xml',
        'views/hms_doctor_views.xml',
        'views/hms_department_views.xml',
        'views/hms_customers_views.xml',
        'reports/hms_patient_template.xml',
        'reports/reports.xml'
    ]
}