from odoo import fields
from odoo import models
from odoo import api


class HrInherit(models.Model):
    _inherit = 'hr.employee'

    is_teacher = fields.Boolean(string="Teacher")




