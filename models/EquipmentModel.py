from odoo import models, fields, api  # pyright: ignore[reportMissingImports]


class EquipmentModel(models.Model):
    _name = 'fixer.equipment.model'
    _description = 'Модель оборудования'
    _parent_name = 'parent_id'
    _parent_store = True
    _order = 'name'

    name = fields.Char(string='Название', required=True)
    parent_id = fields.Many2one('fixer.equipment.model', string='Родительская категория', ondelete='restrict')
    child_ids = fields.One2many('fixer.equipment.model', 'parent_id', string='Подкатегории')
    parent_path = fields.Char(index=True, unaccent=False)
    complete_name = fields.Char(string='Полное название', compute='_compute_complete_name', store=True)

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for rec in self:
            if rec.parent_id:
                rec.complete_name = f'{rec.parent_id.complete_name} / {rec.name}'
            else:
                rec.complete_name = rec.name
