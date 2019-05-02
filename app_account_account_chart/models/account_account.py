# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _


class AccountAccount(models.Model):
    _inherit = "account.account"

    # 图片，可显示小图标，
    # image: all image fields are base64 encoded and PIL-supported
    image = fields.Binary("Image", attachment=True,
        help="This field holds the image used as avatar for this category, limited to 1024x1024px",)
    image_medium = fields.Binary("Medium-sized image", attachment=True,
        help="Medium-sized image of this Category. It is automatically "\
             "resized as a 128x128px image, with aspect ratio preserved. "\
             "Use this field in form views or some kanban views.")
    image_small = fields.Binary("Small-sized image", attachment=True,
        help="Small-sized image of this Category. It is automatically "\
             "resized as a 64x64px image, with aspect ratio preserved. "\
             "Use this field anywhere a small image is required.")

    child_all_count = fields.Integer(
        'Indirect Surbordinates Count',
        compute='_compute_child_all_count', store=False)

    @api.depends('child_ids.child_all_count')
    def _compute_child_all_count(self):
        for rec in self:
            rec.child_all_count = len(rec.child_ids) + sum(child.child_all_count for child in rec.child_ids)
