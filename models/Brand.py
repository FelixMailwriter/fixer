from odoo import models, fields  # pyright: ignore[reportMissingImports]


class Brand(models.Model):
    _name = 'fixer.brand'
    _description = 'Бренд оборудования'
    _order = 'name'

    name = fields.Char(string='Название', required=True)
