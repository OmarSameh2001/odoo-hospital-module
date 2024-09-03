from odoo import fields, models, api


class Shift(models.Model):
    _name = 'shift'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Shift'

    name = fields.Char(string="Shift Name", compute="compute_shift_time", tracking=True)
    date = fields.Date(string="Shift Date", required=True, tracking=True)
    type = fields.Selection([('morning', 'Morning'), ('afternoon', 'Afternoon')
                                , ('night', 'Night')], string="Shift Type", required=True, tracking=True)
    start_time = fields.Datetime(string="Start Time", compute="compute_shift_time", tracking=True)
    end_time = fields.Datetime(string="End Time", compute="compute_shift_time", tracking=True)
    doctor_id = fields.Many2one('doctor', string="Doctor Name", tracking=True, required=True)
    appointment_ids = fields.One2many('appointment', 'shift_id', string="Appointments")


    @api.depends('type')
    def compute_shift_time(self):
        for rec in self:
            if rec.type == 'morning':
                rec.start_time = '08:00:00'
                rec.end_time = '12:00:00'
            elif rec.type == 'afternoon':
                rec.start_time = '12:00:00'
                rec.end_time = '18:00:00'
            elif rec.type == 'night':
                rec.start_time = '18:00:00'
                rec.end_time = '24:00:00'

    @api.depends('date', 'type', 'doctor_id')
    def compute_name(self):
        for rec in self:
            if rec.date and rec.type and rec.doctor_id:
                rec.name = str(rec.doctor_id.name) + ' - ' + str(rec.type) + ' - ' + str(rec.date)

    _sql_constraints = [
        ('unique_doctor_shift_per_day', 'unique(doctor_id, type, date)',
         'A doctor cannot have more than one shift at the same time.')
    ]