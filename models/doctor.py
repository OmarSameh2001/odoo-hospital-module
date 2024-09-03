from odoo import fields, models, api

class Doctor(models.Model):
    _name = 'doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Doctor'

    name = fields.Char(string="Doctor Name", required=True, tracking=True)
    image = fields.Binary(string="Image", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    shift_ids = fields.One2many('shift', 'doctor_id', string="Shifts")