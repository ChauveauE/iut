#-*- coding: utf-8 -*-

from odoo import models, fields, api

class iut_room(models.Model):
    _name = 'iut.room'

    floor = fields.Char()
    name = fields.Char(required=True)

    office_id = fields.Many2one('iut.office', string='office',
    required=True)
    
    partner_ids = fields.One2many('res.partner', 
        'room_id',
        string='partner room')