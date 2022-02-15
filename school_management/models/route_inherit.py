from odoo import fields
from odoo import models


class RouteInherit(models.Model):
    _inherit = 'product.template'

    route_ids = fields.Many2one('stock.location.route')




