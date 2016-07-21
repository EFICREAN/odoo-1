# -*- coding: utf-8 -*-
##############################################################################
#
#    Softlab Perú SAC
#    Copyright (C) 2016-TODAY Tech-Receptives(<http://www.softlabperu.com>)
#    Special Credit and Thanks to Luis Paredes :D
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api
from openerp.report import  report_sxw

class ClinicConsult(models.Model):

    _name = 'clinic.consult'
    _order = "date_appointment desc"

    # @api.one
    # def write(self, values):
    #     obj_consult = self.env['clinic.consult']
    #     pres_line_ids = obj_consult.browse(self.ids[0]).prescription_line_ids
    #
    #     if values.get('prescription_line_ids', False):
    #         obj_pres_line = self.env['clinic.prescription.line']
    #         for pl in pres_line_ids:
    #             exist_pl = False
    #             if pl.prescription_order_id.id:
    #                 exist_pl = True
    #         if exist_pl:
    #             for pl_w in pres_line_ids:
    #                 pl_w.write({
    #                         'prescription_order_id':pl_w.prescription_order_id.id,
    #                 })
    #         else:
    #             #verificamos si existe algún id de consulta en el listado de recetas
    #             exist_consult = False
    #             for pl_c in pres_line_ids:
    #                 if pl_c.consult_id:
    #                     exist_consult = True
    #                     consult_id = pl_c.consult_id.id
    #             new_pres_order_id = self.env['medical.prescription.order'].create({
    #                 'patient_id': obj_consult.browse(self.ids[0]).patient_id.id,
    #                 'physician_id': obj_consult.browse(self.ids[0]).physician_id.id,
    #                 'consult_id': consult_id
    #             })
    #             for pl_w in pres_line_ids:
    #                 pl_w.write({
    #                     'prescription_order_id': new_pres_order_id
    #                 })
    #     return super(ClinicConsult, self).write(values)


    @api.model
    def _get_default_name(self):
        return self.env['ir.sequence'].get('clinic.consult')

    name = fields.Char(required=True, default=_get_default_name, string="Código de consulta")
    patient_id = fields.Many2one('medical.patient','Paciente', required=True)
    date = fields.Datetime("Hora llegada", default=fields.Datetime.now())
    date_appointment = fields.Datetime("Fecha y hora de cita")
    physician_id = fields.Many2one('medical.physician','Médico')
    user_id = fields.Many2one('res.users', related='physician_id.user_id', store=True, string="Usuaio ERP")
    disease_time = fields.Char('Tiempo enfermedad')
    disease_time_current = fields.Text('Enfermedad actual')
    #diagnostic = fields.Text('Diagnóstico')
    plan = fields.Text('Plan')
    physical_exam = fields.Text('Exámen físico')
    treatment_indications = fields.Text('Tratamiento e indicaciones')

    prescription_order_id = fields.Many2one(comodel_name='medical.prescription.order', inverse_name='consult_id', string='Receta')
    prescription_line_ids = fields.One2many('clinic.prescription.line','consult_id', string='Lineas de recetas')
    #prescription_line_ids = fields.One2many(comodel_name='medical.prescription.order', related='prescription_order_id.prescription_line_ids', string='Lineas de receta')
    indication_general = fields.Text(string='Indicaciones generales', related='prescription_order_id.notes')

    testlab_ids = fields.One2many('clinic.testlab', 'consult_id', 'Exámenes laboratorio')
    testimage_ids = fields.One2many('clinic.testimage', 'consult_id', 'Exámenes imágen')
    procedure_ids = fields.One2many('clinic.procedure.line1', 'consult_id', 'Procedimientos')

    age = fields.Char(string='Edad', related='patient_id.age')
    identification_code = fields.Char('Identificación Interna', related="patient_id.identification_code")



    fam_asthma = fields.Selection([('yes', 'Si'), ('no', 'No')],string='Asma', related='patient_id.fam_asthma' )
    fam_cardiovascular = fields.Selection([('yes', 'Si'), ('no', 'No')],string='Enfermedades cardiovasculares', related='patient_id.fam_cardiovascular')
    fam_diabetic = fields.Selection([('yes', 'Si'), ('no', 'No')],string='Diabetes', related='patient_id.fam_diabetic')
    fam_allergy = fields.Selection([('yes', 'Si'), ('no', 'No')],string='Alergias', related='patient_id.fam_allergy')
    fam_cancer = fields.Selection([('yes', 'Si'), ('no', 'No')],string='Cancer', related='patient_id.fam_cancer')
    fam_infectious = fields.Selection([('yes', 'Si'), ('no', 'No')],string='Enfermedades infectocontagiosas',related='patient_id.fam_infectious')
    fam_specify = fields.Text('Otros', related='patient_id.fam_specify')


    per_asthma = fields.Selection([('yes', 'Si'), ('no', 'No')],string='Asma', related='patient_id.per_asthma')
    per_cardiovascular = fields.Selection([('yes', 'Si'), ('no', 'No')],string='Enfermedades cardiovasculares', related='patient_id.per_cardiovascular')
    per_diabetic = fields.Selection([('yes', 'Si'), ('no', 'No')],string='Diabetes', related='patient_id.per_diabetic')
    per_allergy = fields.Selection([('yes', 'Si'), ('no', 'No')],string='Alergias', related='patient_id.per_allergy')
    per_cancer = fields.Selection([('yes', 'Si'), ('no', 'No')],string='Cancer', related='patient_id.per_cancer')
    per_infectious = fields.Selection([('yes', 'Si'), ('no', 'No')],string='Enfermedades infectocontagiosas', related='patient_id.per_infectious')
    per_specify = fields.Text('Otros', related='patient_id.per_specify')


    triage_id = fields.Many2one(
        comodel_name='patient.triage',
        string='Preconsulta'
    )

    blood_pressure = fields.Char(string = '[PA]', related='triage_id.blood_pressure')
    saturation_oxigen = fields.Char('[SatO]', related='triage_id.saturation_oxigen')
    temperature_ammount = fields.Integer('[T]', related='triage_id.temperature_ammount')
    state = fields.Selection(
        [('draft','Nueva'),('pay','Pagado'),('pre_consult', 'Preconsulta'), ('process', 'En consulta'),
         ('done', 'Realizado'), ('cancel', 'Anulado')], 'Estado', default='draft'
    )
    consulttype_id = fields.Many2one(
        comodel_name='clinic.consult.type', required=True, index=True, string='Tipo consulta')

    disease_ids = fields.One2many(
        comodel_name='medical.patient.disease', inverse_name='consult_id',
        string='Diagnóstico')

    @api.one
    def draft_pay(self):
        self.write({'state': 'pay'})
        return True

    @api.one
    def pay_pre_consult(self):
        self.write({'state': 'pre_consult'})
        return True

    @api.one
    def pre_consult_process(self):
        if not self.prescription_order_id:
            obj_prescription=self.env['medical.prescription.order']
            prescription_id = obj_prescription.create({
                'patient_id': self.patient_id.id,
                'physician_id': self.physician_id.id,
                'date_prescription': self.date_appointment,
                'consult_id':self.id
            })
        self.write({'state': 'process',
                    'prescription_order_id': prescription_id.id})
        return True

    @api.one
    def process_done(self):
        if self.prescription_order_id:
            prescription_order=self.prescription_order_id
            obj_prescription = self.env['medical.prescription.order']
            if len(prescription_order.prescription_line_ids)==0:
                prescription_order.unlink()
            else:
                prescription_order.write({
                     'date_prescription':fields.Datetime.now()
                })
        self.write({'state': 'done',
                    })
        return True

    @api.one
    def to_cancel(self):
        self.write({'state': 'cancel'})
        return True