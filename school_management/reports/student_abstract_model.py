from odoo import api, models, fields


class StudentResult(models.AbstractModel):
    _name = 'report.school_management.report_student_result'
    _description = 'Student Result'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("docids", docids)
        print("data ", data)
        domain = []
        name = data.get('form').get('student_id')
        date_from = data.get('form').get('date_from')
        date_to = data.get('form').get('date_to')

        if name:
            domain += [('student_id', '=' , name[1])]
        if date_from:
            domain += [('date', '>=' , date_from)]
        if date_to:
            domain += [('date', '<=' , date_to)]
        print(domain)

        docs = self.env['student.result'].search(domain)


        return {
            # 'doc_model': 'student.result',
            'data': data,
            'docs': docs,
        }
