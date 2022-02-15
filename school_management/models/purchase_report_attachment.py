import base64
from odoo import models


class PurchaseReportAttachment(models.Model):
    _inherit = "purchase.order"

    def action_sent_mail(self):
        if self.state == 'draft':
            template_id = self.env['ir.model.data']._xmlid_lookup('school_management.purchase_order_mail_template')
            # print(template_id[2])
            # template_ids = self.env.ref('school_management.purchase_order_mail_template')
            # print(template_ids[0])
            ctx = {
                'default_model': 'purchase.order',
                'active_model': 'purchase.order',
                'active_id': self.id,
                'default_res_id': self.id,
                'default_use_template': bool(template_id),
                'default_template_id': template_id[2],
                'default_composition_mode': 'comment',
                'custom_layout': "mail.mail_notification_paynow",
                'force_email': True,
                'mark_rfq_as_sent': True,
            }

            return {
                'name': 'Purchase RFQ',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'mail.compose.message',
                'target': 'new',
                'context':ctx,
            }

        # template_id.send_mail(self.id, force_send=True)

    def button_confirm(self):
        super(PurchaseReportAttachment, self).button_confirm()
        self.action_get_attachment()
        return self.env.ref('purchase.action_report_purchase_order').report_action(self)

    def action_get_attachment(self):
        pdf = self.env.ref('purchase.action_report_purchase_order')._render_qweb_pdf(self.ids)
        b64_pdf = base64.b64encode(pdf[0])
        # save pdf as attachment
        name = "My Attachment"
        return self.env['ir.attachment'].create({
            'name': name,
            'type': 'binary',
            'datas': b64_pdf,
            'res_model': self._name,
            'res_id': self.id,
            'mimetype': 'application/x-pdf'
        })
