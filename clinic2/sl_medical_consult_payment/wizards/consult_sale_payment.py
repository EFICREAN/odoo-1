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
import openerp.addons.decimal_precision as dp

class Consult_Sale_Wizard(models.TransientModel):
    _name = 'consult.sale.wizard'

    consult_id = fields.Many2one(
        string='Consulta',
        comodel_name='clinic.consult',
        required=True,
    )
    product_tmpl_id = fields.Many2one(
        string='Servicio',
        comodel_name='product.template',
        required=True,
        related='consult_id.consulttype_id.product_tmpl_id'
    )
    pricelist_id = fields.Many2one(
        string='Tarifa',
        comodel_name='product.pricelist',
        required=True,
    )
    # currency_id = fields.Many2one(
    #     string='Moneda',
    #     comodel_name='res.currency',
    # )
    date_order = fields.Datetime(
        string='Fecha',
    )
    company_id = fields.Many2one(
        string='Compañia',
        comodel_name='res.company',
    )

    note = fields.Text()

    @api.one
    def make_invoice_workflow(self, vals_order={}):
        obj_order = self.env['sale.order']
        invoice_obj = self.env['account.invoice']

        vals_order['user_id'] = self._uid
        new_id = obj_order.create(vals_order)

        #automatiza el flujo normal hasta la factura
        new_id.signal_workflow("order_confirm")
        new_id.signal_workflow("manual_invoice")
        inv_id=invoice_obj.search([
            ('origin', '=', new_id.name)
        ], limit=1)
        #inv_id.signal_workflow("invoice_open")
        return inv_id

    @api.multi
    def make_invoice(self, ):
        partner = self.consult_id.patient_id.partner_id
        fpos = partner.property_account_position and partner.property_account_position.id or False
        payment_term = partner.property_payment_term and partner.property_payment_term.id or False
        #partner_addr = partner_obj.address_get(self._cr, self._uid, [partner.id],
        #                                      ['default', 'invoice', 'delivery', 'contact'])

        if self._context.get('create_consult', False):
            order_line=[]
            order_line.append((0,
                                  0,
                                  {
                                   'product_id': self.consult_id.consulttype_id.product_id.id,
                                   'name': self.consult_id.consulttype_id.name,
                                   'quantity': 1,
                                   'price_unit': self.consult_id.consulttype_id.product_tmpl_id.list_price
                                   }))


        # if self._context.get('invoice_examlab', False):
        #     order_line = []
        #     for t in self.consult_id.testlab_ids:
        #         order_line.append((0,
        #                            0,
        #                            {
        #                                'product_id': t.testtype_id.product_id.id,
        #                                'name':  t.testtype_id.product_id.name,
        #                                'quantity': 1,
        #                                'price_unit':  t.testtype_id.product_id.product_tmpl_id.list_price
        #                            }))
        # if self._context.get('invoice_examimage', False):
        #     order_line = []
        #     for t in self.consult_id.testimage_ids:
        #         order_line.append((0,
        #                            0,
        #                            {
        #                                'product_id': t.testtype_id.product_id.id,
        #                                'name': t.testtype_id.product_id.name,
        #                                'quantity': 1,
        #                                'price_unit':  t.testtype_id.product_id.product_tmpl_id.list_price
        #                            }))
        # if self._context.get('invoice_procedure', False):
        #     order_line = []
        #     for t in self.consult_id.procedure_ids:
        #         order_line.append((0,
        #                            0,
        #                            {
        #                                'product_id': t.procedure_id.product_id.id,
        #                                'name': t.procedure_id.product_id.name,
        #                                'quantity': 1,
        #                                'price_unit':  t.procedure_id.product_id.product_tmpl_id.list_price
        #                            }))
        # if self._context.get('invoice_prescription', False):
        #     order_line = []
        #     for t in self.consult_id.prescription_line_ids:
        #         order_line.append((0,
        #                            0,
        #                            {
        #                                'product_id': t.medicament_id.product_id.id,
        #                                'name': t.medicament_id.product_id.name,
        #                                'quantity': 1,
        #                                'price_unit':  t.medicament_id.product_id.product_tmpl_id.list_price
        #                            }))
        vals_consult = {'origin': self.consult_id.name,
                'partner_id': partner.id,
                'pricelist_id': self.pricelist_id.id,
                # 'partner_invoice_id': partner_addr['invoice'],
                'partner_invoice_id': partner.id,
                # 'partner_shipping_id': partner_addr['delivery'],
                'partner_shipping_id': partner.id,
                'date_order': fields.datetime.now(),
                'fiscal_position': fpos,
                'payment_term': payment_term,
                'order_line': order_line,
                }

        inv_id = self.make_invoice_workflow(vals_consult)

        if self._context.get('create_consult', False):
            self.consult_id.write({
                'state': 'pre_consult'
            })
        if self._context.get('create_consult', False):
            ir_model_data = self.env['ir.model.data']
            form_res = ir_model_data.get_object_reference('account', 'invoice_form')
            form_id = form_res and form_res[1] or False

            res = {
                'view_mode': 'form',
                'nodestroy': True,
                'name': u'Comprobante de cliente',
                'context': "{'type':'out_invoice'}",
                'view_type': 'form',
                'res_model': 'account.invoice',
                'view_id': [(form_id,)],
                'type': 'ir.actions.act_window',
                'res_id': inv_id[0].id,
                'target': 'current'}

            return res
        return {'type': 'ir.actions.act_window_close'}



