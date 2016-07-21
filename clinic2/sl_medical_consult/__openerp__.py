{
    'name': 'Medical consult',
    'version': '8.0.1.1.0',
    'category': 'Clinic',
    'depends': [
        'medical_prescription',
        'sl_medical_testlab',
        'sl_clinic_procedure',
        'sl_medical_disease',
        'sl_patient_triage',
        'sl_medical_testlab',
    ],
    'author': 'Luis Paredes para Softlab Perú SAC',
    'website': 'http://www.softlabperu.com',
    'license': 'AGPL-3',
    'data': [
        'data/ir_sequence.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
