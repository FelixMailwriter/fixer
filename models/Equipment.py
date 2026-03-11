from odoo import models, fields # pyright: ignore[reportMissingImports]

class Equipment(models.Model):
    _name = 'fixer.equipment'
    _description = 'Describe equipment that workman can use'

    name = fields.Char(string='Название', required=True)
    description = fields.Text(string='Описание')

