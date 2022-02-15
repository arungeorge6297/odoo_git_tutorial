from odoo import fields
from odoo import models

class StudentResult(models.Model):
    _name = 'student.result'
    _rec_name = 'subject_id'


    subject_id = fields.Many2one('subject.list')
    mark = fields.Float(default=0.0)
    student_id = fields.Many2one('student.management')
    date = fields.Date(string="Date")
