{
    'name': 'Clinic inpatient admission view',
    'version': '8.0.1.1.0',
    'category': 'Clinic',
    'depends': [
        'medical',
        'medical_his',
        'medical_disease',
        'sl_medical_inpatient_admission',
        'sl_medical_inpatient_admission_prescription'
    ],
    'author': 'Luis Paredes para Softlab Perú SAC',
    'website': 'http://www.softlabperu.com',
    'license': 'AGPL-3',
    'data': [
        'views/evaluations_lines_admission.xml',
        'views/indications_lines_admission.xml',
        'views/inpatient_admission.xml',
    ],
    'installable':True,
    'application': True,
    'auto_install': False,
}
