from openerp import fields, models


class ProductTemplateProcedure(models.Model):
    _inherit = 'product.template'

    is_procedure = fields.Boolean()