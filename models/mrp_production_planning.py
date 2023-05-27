# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT



class MrpProductionPlanningLine(models.Model):
    _inherit = 'mrp.production.planning.line'

    sale_id = fields.Many2one('sale.order','Sales order',related='mrp_production_request_id.sale_id')
    sale_line_id = fields.Many2one('sale.order.line', 'Sale Line', related='mrp_production_request_id.sale_line_id')
    partner_id = fields.Many2one('res.partner', string='Customer', related='mrp_production_request_id.partner_id')
    client_order_ref = fields.Char(string='Customer Reference',related='mrp_production_request_id.client_order_ref')
