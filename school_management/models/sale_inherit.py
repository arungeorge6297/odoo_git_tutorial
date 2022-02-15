import base64

from odoo import fields
from odoo import models
from odoo import api


class SaleInherit(models.Model):
    _inherit = 'sale.order'

    # purchase_line_ids = fields.Many2one('purchase_line_ids', string="Purchase Lines")
    purchase_info = fields.One2many('purchase.info', 'info_id', readonly=True)



    # @api.constrains('order_line')
    # def _compute_purchase_info(self):
    #     lines = []
    #     for rec in self.order_line:
    #         # print(rec.product_id.seller_ids)
    #         route = rec.product_id.route_ids.name
    #         print(route)
    #         if route == 'Dropship':
    #             product_id = rec.product_id.id
    #             print(product_id)
    #             purchase = self.env['purchase.order'].search([('product_id', '=', product_id)])
    #             print(purchase)
    #
    #
    #             for d in purchase:
    #                 print(d.id)
    #                 po_number = d.name
    #                 print(po_number)
    #                 vendor_name = d.partner_id.name
    #                 print(vendor_name)
    #
    #
    #                 lines.append((0,0,{
    #                     'po_number': po_number,
    #                     'vendor_name' : vendor_name,
    #                     'info_id' : d.id
    #                 }))
    #
    #                 print(lines)
    #                 print(type(lines))
    #
    #     self.purchase_info = lines

    def action_confirm(self):
        super(SaleInherit, self).action_confirm()
        lines = []
        for rec in self.order_line:
            routes = rec.product_id.route_ids.name
            print(routes)
            for route in routes:
                if route == 'Dropship':
                    product_id = rec.product_id.id
                    print(product_id)
                    po_no = rec.purchase_line_ids.order_id.name
                    vendor_name = rec.purchase_line_ids.partner_id.name

                    lines.append((0,0,{
                        'po_number' : po_no,
                        'vendor_name' : vendor_name,
                    }))

        print(lines)

        self.purchase_info = lines
