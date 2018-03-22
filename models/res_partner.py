#-*- coding: utf-8 -*-

from odoo import models, fields, api

class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = "res.partner"

    employee_ref = fields.Char(required=True)

    device_ids = fields.One2many('iut.it.device', 
        'partner_id',
        string='device partner')
    
    room_id = fields.Many2one('iut.room', string='room',
    required=True)