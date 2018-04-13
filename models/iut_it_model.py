#-*- coding: utf-8 -*-

from odoo import models, fields, api

class iut_it_model(models.Model):
    _name = 'iut.it.model'

    name = fields.Char(required=True)
    ref = fields.Char()

    type_ids = fields.Many2many('iut.it.model.type', string='model_type')

    brand_id = fields.Many2one('iut.it.brand', string='brand')
    devices_ids = fields.One2many('iut.it.device', 'model_id', string='device model')