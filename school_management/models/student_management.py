from odoo import fields, models, api
import datetime, re
from datetime import date
from odoo.exceptions import UserError, ValidationError


class StudentManagement(models.Model):
    _name = 'student.management'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "It's a  details about student information"
    _order = "admission_date desc"

    name = fields.Char(string="Student Name")
    roll_no = fields.Integer(string="Roll Number")
    street = fields.Char()
    street2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state')
    zip = fields.Char()
    country_id = fields.Many2one('res.country')
    bdate = fields.Date(string="Birth Date")
    admission_date = fields.Date(string="Admission Date")
    standard = fields.Integer(string="Standard")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", default='male')
    student_image = fields.Binary()
    student_documents = fields.Many2many('ir.attachment')
    contact_number = fields.Char(string="Contact Number", size=10)
    guardian_name = fields.Char(string="Guardian Name")
    school_id = fields.Many2one('school.management', string="School")
    student_age = fields.Char(string="Age", compute="_compute_student_age")
    email = fields.Char(string="Email")
    result_ids = fields.One2many('student.result','student_id')
    teacher_id = fields.Many2one('hr.employee', string="Teacher", domain="[('is_teacher', '=' , True)]")

    @api.model
    def create(self,values):
        print("values of values:", values)
        print("self:", self)
        rtn = super(StudentManagement, self).create(values)
        print("rtn:",rtn)
        return rtn
    #No decorator
    def write(self, values):
        print("values:",values)
        rtn = super(StudentManagement, self).write(values)
        print("rtn:", rtn)
        return rtn

    def copy(self, default=None):
        print("default:",default)
        rtn = super(StudentManagement, self).copy(default= default)
        print("rtn:", rtn)
        return rtn

    @api.depends('bdate')
    def _compute_student_age(self):
        todays_date = datetime.date.today()
        for rec in self:
            if rec.bdate:
                bdate = fields.Datetime.to_datetime(rec.bdate).date()
                age = str(int((todays_date - bdate).days / 365))
                rec.student_age = age
            else:
                rec.student_age = "Not Provided"

    @api.constrains('contact_number')
    def is_valid_number(self):
        l = len(self.contact_number)
        for ch in self.contact_number:
            letter = ch.isalpha()
            if letter:
                raise ValidationError("Enter only Numbers")
            elif l != 10:
                raise ValidationError("Enter 10 Number")

    def action_send_mail(self):
        template_id = self.env.ref('school_management.student_detail_email_template')
        template_id.send_mail(self.id, force_send=True)

    _sql_constraints = [
        ('roll_no', 'CHECK(roll_no > 0)',
         'The Roll Number should be greater than zero')
    ]
