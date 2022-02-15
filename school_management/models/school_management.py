from odoo import fields, models, api


class SchoolManagement(models.Model):
    _name = 'school.management'
    _description = "It's a sample details about school management"
    _order = "sequence, rank"


    name = fields.Char(string="School Name")
    description = fields.Text(string="Description")
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better")
    street = fields.Char()
    street2 = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one('res.country.state')
    zip = fields.Char()
    country_id = fields.Many2one('res.country')
    win_percentage = fields.Float(string="Win Percentage")
    school_image = fields.Binary(string="School Image")
    rank = fields.Char(string="School Rank")
    students_ids = fields.One2many('student.management', 'school_id', string="Students")
    state = fields.Selection([('new', 'New'), ('confirmed', 'Confirmed')], default='new')
    tag_ids = fields.Many2many('school.tags', string="School Type")
    teacher_ids = fields.One2many('teacher.management', 'school_id', string="Teachers")

    @api.onchange('win_percentage')
    def _onchange_rank(self):
        if self.win_percentage < 30:
            self.rank = "Not Available"

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'
        return True

    def action_cancel(self):
        for rec in self:
            rec.state = 'new'
        return True
