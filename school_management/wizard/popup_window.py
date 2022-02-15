from odoo import models
from odoo import fields


class PopupWindow(models.TransientModel):
    _name = 'popup.window'

    student_id = fields.Many2one('student.management')
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def action_sent_mail(self):
        print('self.read:',self.read())
        print(self.read()[0])
        # domain = []
        # if self.student_id:
        #     domain += [('student_id', '=' , self.student_id.id)]
        # if self.date_from:
        #     domain += [('date', '>=' , self.date_from)]
        # if self.date_to:
        #     domain += [('date', '<=' , self.date_to)]

        # result_list = self.env['student.result'].search_read(domain)

        data = {
            'form': self.read()[0],
            # 'result': result_list,
        }
        return self.env.ref('school_management.report_student_results').report_action(self, data=data)




