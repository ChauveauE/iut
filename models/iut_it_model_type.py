#-*- coding: utf-8 -*-

from odoo import models, fields, api

class iut_it_model_type(models.Model):
    _name = 'iut.it.model.type'

    name = fields.Char(required=True)

    model_ids = fields.Many2many('iut.it.model', string='model')