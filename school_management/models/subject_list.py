from odoo import models
from odoo import fields

class SubjectList(models.Model):
    _name = 'subject.list'

    name = fields.Char(string="Create a new subject")