#-*- coding: utf-8 -*-

from odoo import models, fields, api

class iut_office(models.Model):
    _name = 'iut.office'
    _inherit = "res.partner"

    #employee_nb = fields.Integer(compute='')
    room_ids = fields.One2many('iut.room', 
        'office_id',
        string='room office')
