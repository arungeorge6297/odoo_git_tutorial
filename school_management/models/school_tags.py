from odoo import fields, models


class SchoolTags(models.Model):
    _name = 'school.tags'

    name = fields.Char(string="School Type")
