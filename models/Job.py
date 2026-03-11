from odoo import models, fields

class Job(models.Model):
    _name = 'fixer.job'
    _description = 'Describe jobs that workman can perform'

    name = fields.Char(string='Название', required=True)
    description = fields.Text(string='Описание')

