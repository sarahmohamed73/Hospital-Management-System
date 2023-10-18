from odoo import fields , models, api
from odoo.exceptions import  ValidationError, UserError
class HMS_Customers(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient')

    _sql_constraints = [
        ('unique_patient', 'UNIQUE(related_patient_id)', 'This Patient Already Linked To Another Customer')
    ]

    # @api.constrains('related_patient_id')
    # def valid_email(self):
    #     if self.env['res.partner'].search([("related_patient_id.email", "=", self.related_patient_id.email)], limit=1):
    #             raise ValidationError('This Patient Already Exist To Another Customer')
        
    def unlink(self):
        for record in self :
            if record.related_patient_id:
                raise UserError('This Customer Is Linked To A Patient')