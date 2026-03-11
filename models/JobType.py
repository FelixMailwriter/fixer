from odoo import models, fields

class JobType(models.Model):
    _name = 'fixer.jobtype'
    _description = 'Describe jobs types that workman can perform'

    name = fields.Char(string='Название', required=True)
    description = fields.Text(string='Описание')

