from openerp import fields, models


class ProductTemplateConsult(models.Model):
    _inherit = 'product.template'

    is_consult = fields.Boolean()