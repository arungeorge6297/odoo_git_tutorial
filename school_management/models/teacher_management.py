import datetime
from odoo import fields
from odoo import models
from odoo import api


class TeacherManagement(models.Model):
    _name = 'teacher.management'
    _description = "All details about our faculty"
    _order = "name desc"



    name = fields.Char(string="Teacher Name")
    street = fields.Char()
    street2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state')
    zip = fields.Char()
    country_id = fields.Many2one('res.country')
    bdate = fields.Date(string="Birth Date")
    employee_id = fields.Char("Employee ID", readonly=True, copy=False, required=True, index=True, default='New')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", default='male')
    teacher_image = fields.Binary(string="Teacher Image")
    contact_number = fields.Integer(string="Contact Number")
    subject = fields.Selection([
        ('maths', 'Maths'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('biology', 'Biology'), ('it', 'IT')],
        string="Subject", default='maths')
    school_id = fields.Many2one('school.management', string="School")
    teacher_age = fields.Char(string="Age", compute="_compute_teacher_age")


    @api.depends('bdate')
    def _compute_teacher_age(self):
        todays_date = datetime.date.today()
        for rec in self:
            if rec.bdate:
                bdate = fields.Datetime.to_datetime(rec.bdate).date()
                age = str(int((todays_date - bdate).days / 365))
                rec.teacher_age = age
            else:
                rec.teacher_age = "Not Provided"

    @api.model
    def create(self, vals):
        if vals.get('employee_id', 'New') == 'New':
            vals['employee_id'] = self.env['ir.sequence'].next_by_code('teacher.sequence') or 'New'
        return super(TeacherManagement, self).create(vals)
