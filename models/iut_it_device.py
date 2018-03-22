#-*- coding: utf-8 -*-

from odoo import models, fields, api

class iut_it_device(models.Model):
    _name = 'iut.it.device'

    name = fields.Char(required=True)
    date_allocation = fields.Date()
    serial_number = fields.Integer(required=True)
    date_purchase = fields.Date()
    date_warranty_end = fields.Date()

    partner_id = fields.Many2one('res.partner', string='employee',
    required=True)

    model_id = fields.Many2one('iut.it.model', string='model',
    required=True)

    room_id = fields.Integer(related='partner_id.room_id.id',store=True)
    office_id = fields.Integer(related='partner_id.room_id.office_id.id', store=True)