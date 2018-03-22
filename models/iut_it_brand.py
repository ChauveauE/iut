#-*- coding: utf-8 -*-

from odoo import models, fields, api

class iut_it_brand(models.Model):
    _name = 'iut.it.brand'

    name = fields.Char(required=True)
    warranty_delay_month = fields.Integer()
    support_phone = fields.Integer()

    models_ids = fields.One2many('iut.it.model', 
        'brand_id',
        string='model brand')