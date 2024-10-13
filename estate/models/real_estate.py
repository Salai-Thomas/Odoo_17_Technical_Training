from odoo import fields, models, api
class RealEstate(models.Model):
    _name = 'real.estate'
    _description = 'Test model'

    name = fields.Char(string="Name")
    price = fields.Float(string="Float")
