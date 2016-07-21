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


class Testlab_Sale_Wizard(models.TransientModel):
    _name = 'testlab.sale.wizard'

    testlab_line_id = fields.Many2one(
        string='Prueba laboratorio',
        comodel_name='clinic.testlab',
        required=True,
    )
    partner_id = fields.Many2one(
        string='Cliente',
        comodel_name='res.partner',
        required=True,
        related='testlab_line_id.patient_id.partner_id'
    )

    product_tmpl_id = fields.Many2one(
        string='Servicio',
        comodel_name='product.template',
        required=True,
        related='testlab_line_id.testtype_id.product_tmpl_id'
    )

    @api.multi
    def add_sale(self, ):
        obj_order = self.env['sale.order']
        obj_order_line = self.env['sale.order.line']
        partner = self.testlab_line_id.patient_id.partner_id
        patient = self.testlab_line_id.patient_id
        order = self.testlab_line_id.patient_id.sale_order_id
        fpos = partner.property_account_position and partner.property_account_position.id or False
        payment_term = partner.property_payment_term and partner.property_payment_term.id or False
        #partner_addr = partner_obj.address_get(self._cr, self._uid, [partner.id],
        #                                      ['default', 'invoice', 'delivery', 'contact'])
        order_line = []
        order_line.append((0,
                           0,
                           {
                               'product_id': self.testlab_line_id.testtype_id.product_id.id,
                               'name': self.testlab_line_id.testtype_id.product_id.name,
                               'quantity': 1,
                               'price_unit': self.testlab_line_id.testtype_id.product_tmpl_id.list_price
                           }))

        if not order or order.state != 'draft':
            vals_sale = {'origin': self.testlab_line_id.name, 'partner_id': partner.id,
                         'partner_invoice_id': partner.id,
                         'partner_shipping_id': partner.id, 'date_order': fields.datetime.now(),
                         'fiscal_position': fpos, 'payment_term': payment_term, 'order_line': order_line,
                         'user_id': self._uid}
            order_new_id = obj_order.create(vals_sale)
            sale_line_id = obj_order_line.search([('order_id','=',order_new_id.id),('product_id','=', self.testlab_line_id.testtype_id.product_id.id)])

            self.testlab_line_id.write({
                'sale_order_id':sale_line_id[0].id
            })
            patient.write({
                'sale_order_id': order_new_id.id,
            })
            id_sale = order_new_id.id
        if order and order.state == 'draft':
            order.write({
                'order_line': order_line,
            })
            sale_line_id = obj_order_line.search([('order_id', '=', order.id), ('product_id', '=', self.testlab_line_id.testtype_id.product_id.id)])
            self.testlab_line_id.write({
                'sale_order_id': sale_line_id[0].id,
            })
            id_sale = order.id

        if self._context.get('view_testlab', False):
            ir_model_data = self.env['ir.model.data']
            form_res = ir_model_data.get_object_reference('sale', 'view_order_form')
            form_id = form_res and form_res[1] or False

            res = {
                'view_mode': 'form',
                'nodestroy': True,
                'name': u'Pedido de venta',
                'view_type': 'form',
                'res_model': 'sale.order',
                'view_id': [(form_id,)],
                'type': 'ir.actions.act_window',
                'res_id': id_sale,
                'target': 'current'}
            return res
        return {'type': 'ir.actions.act_window_close'}
