from openerp import fields, models


class Product_Template_Test(models.Model):
    _inherit = 'product.template'

    is_testimage = fields.Boolean()
    is_testlab = fields.Boolean()