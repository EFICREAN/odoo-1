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
from openerp import models,fields, api,exceptions, tools
from openerp.report import  report_sxw
from datetime import time, timedelta, datetime
import logging



class InpatientAdmission(models.Model):

    _name = 'inpatient.admission'

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
        return self.env['ir.sequence'].get('inpatient.admission')

    name = fields.Char(required=True, default=_get_default_name, string="Código de hopitalización")
    patient_id = fields.Many2one('medical.patient','Paciente', required=True)
    admission_date = fields.Datetime("Fecha de Hospitalización", default=fields.Datetime.now())
    discharge_date = fields.Datetime("Fecha de Alta")
    attending_physician = fields.Many2one('medical.physician','Médico que atiende')
#    operationg_physician = fields.Many2one('medical.physician', 'Médico que opera')
    admission_reason = fields.Many2one('medical.pathology', 'Razón de admisión')
    admission_type = fields.Selection([('routine','Rutina'),('maternity','maternidad'),
                                       ('elective','Electivo'),('urgent','Urgencia'),
                                       ('emergency','Emergencia'),('other','Otros'),
                                       ('interconsult','interconsulta')],'Tipo de admisión')
    room = fields.Many2one('medical.hospital.room', 'Cuarto de hospital', required=True)
    bed = fields.Many2one('medical.hospital.bed', 'Cama de hospital', required=True)
    discharge_plan = fields.Text('Plan de Alta')
    info = fields.Text('Información extra')

    #prescription_ids = fields.One2many('medical.prescription.order', 'consult_id', 'Receta')

    testlab_ids = fields.One2many('clinic.testlab','admission_id',string='Exámen laboratorio')

    testimage_ids = fields.One2many('clinic.testimage','admission_id', string='Exámen imágen')

    evaluation_line_ids = fields.One2many('evaluation.lines','inpatient_admission_id', string='Evaluación Hospitalarias')

    plan_line_ids = fields.One2many(comodel_name='plan.line', inverse_name='inpatient_admission_id', string='Indicaciones Hospitalarias')

    procedure_line_ids = fields.One2many(
        comodel_name='clinic.procedure.line1', inverse_name='inpatient_admission_id', string='Procedimientos'
    )
    state = fields.Selection(
        [('draft','Nueva'),('hospitalized','Hospitalizado'),('invoiced', 'Facturado'), ('discharged', 'De Alta'),
         ('cancel','Cancelado')],
         'Estado', default='draft'
    )
    sale_order_id = fields.Many2one(comodel_name='sale.order', string='Pedido')
    order_line = fields.One2many(comodel_name='sale.order.line', string='Detalle', related='sale_order_id.order_line', readonly=False)

    #Anamnesis
    disease_current = fields.Char(string='Enfermedad actual')
    form_home = fields.Char(string='Forma de inicio')
    course = fields.Char(string='Curso')
    signs_symptoms = fields.Text(string='Signos y síntomas')
    related = fields.Text(string='Relato (Cronológico y Descriptivo)')

    #Funciones biológicas
    thirst = fields.Selection([
        ('si','SI'),('no','No'), ('no_define', 'No definido')
    ], 'Sed', default='no_define')
    dream = fields.Selection([
        ('si', 'SI'), ('no', 'No'), ('no_define', 'No definido')
    ], 'Sueño', default='no_define')
    sweat = fields.Selection([
        ('si', 'SI'), ('no', 'No'), ('no_define', 'No definido')
    ], 'Sudor', default='no_define')
    appetite  = fields.Selection([
        ('si', 'SI'), ('no', 'No'), ('no_define', 'No definido')
    ], 'Apeito', default='no_define')
    weight = fields.Selection([
        ('si', 'SI'), ('no', 'No'), ('no_define', 'No definido')
    ], 'Peso', default='no_define')
    urine = fields.Selection([
        ('si', 'SI'), ('no', 'No'), ('no_define', 'No definido')
    ], 'Orina', default='no_define')
    laxatives = fields.Selection([
        ('si', 'SI'), ('no', 'No'), ('no_define', 'No definido')
    ], 'Laxantes', default='no_define')
    sedative = fields.Selection([
        ('si', 'SI'), ('no', 'No'), ('no_define', 'No definido')
    ], 'Sedantes', default='no_define')

    #Exámen físico
    skin = fields.Char(string='Piel')
    head_neck = fields.Char(string='Cabeza y cuello')
    thorax_lung = fields.Char(string='Tórax y pulmon')
    cardiovascular = fields.Char(string='Cardiovascular')
    abdomen_rectum = fields.Char(string='Abdon y recto')
    genitourinary = fields.Char(string='Aparato genito urinario')
    neurological = fields.Char(string='Exámen neurológico')
    #Diagnóstico
    diagnosis = fields.Text(string='Diagnóstico')

    @api.one
    def s_draft(self):
        self.write({'state': 'draft'})
        return True

    @api.one
    def s_hospitalized(self):
        self.write({'state': 'hospitalized'})
        bed_room=self.env['medical.hospital.bed'].search([('name', '=', self.bed.name)])
        bed_room.write({'state': 'occupied'})
        room_bed = self.env['medical.hospital.room'].search([('name', '=', self.bed.room_id.name)])
        room_type = self.asig_rooms(room_bed)
        if room_type == 'full':
            room_bed.write({'state': 'full'})
        else:
            room_bed.write({'state' : 'beds_available'})
        return True

    @api.multi
    def asig_rooms(self,room_bed):
        state_room = 'full'
        _logger = logging.getLogger(__name__)
        for record in room_bed.bed_ids:
            _logger.info('valor de %s es %s',record.name,record.state)
            if record.state == 'free':
                state_room= 'beds_available'

        return state_room

    @api.one
    def s_invoiced(self):
        self.write({'state': 'invoiced'})
        return True

    @api.one
    def s_discharged(self):
        self.write({'state': 'discharged'})
        self.env['medical.hospital.bed'].search([('name', '=', self.bed.name)]).write({'state': 'free'})
        room_bed = self.env['medical.hospital.room'].search([('name', '=', self.bed.room_id.name)])
        room_type = self.asig_rooms(room_bed)
        if room_type == 'full':
            room_bed.write({'state': 'full'})
        else:
            room_bed.write({'state': 'beds_available'})
        return True

    @api.one
    def s_cancel(self):
        self.write({'state': 'cancel'})
        self.env['medical.hospital.bed'].search([('name', '=', self.bed.name)]).write({'state': 'free'})
        room_bed = self.env['medical.hospital.room'].search([('name', '=', self.bed.room_id.name)])
        room_type = self.asig_rooms(room_bed)
        if room_type == 'full':
            room_bed.write({'state': 'full'})
        else:
            room_bed.write({'state': 'beds_available'})
        return True
