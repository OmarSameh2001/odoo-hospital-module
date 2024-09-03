from odoo import fields, models, api


class HospitalAppointment(models.Model):
    _name = 'appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'

    patient_id = fields.Many2one('patient', string="Patient Name", tracking=True)
    age = fields.Integer(string="Patient Age", related='patient_id.age', readonly=True)
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('other', 'Other')
                               ], string="Patient Gender", related='patient_id.gender', readonly=True)
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference", tracking=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirm'),
                              ('done', 'Done'),
                              ('cancel', 'Cancel')
                              ], string="State", default='draft', tracking=True)

    @api.model
    def create(self, vals):
        res = super(HospitalAppointment, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('property.ref')
        return res