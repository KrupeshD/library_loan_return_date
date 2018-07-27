# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class library_loan_return_date(models.Model):
#     _name = 'library_loan_return_date.library_loan_return_date'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100