import base64
from odoo import fields
from odoo import models


class PurchaseInfo(models.Model):
    _name = 'purchase.info'

    po_number = fields.Char(string="Purchase Number")
    vendor_name = fields.Char(string="Vendor Name")
    info_id = fields.Many2one('sale.order')
