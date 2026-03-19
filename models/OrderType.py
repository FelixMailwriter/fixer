from odoo import models, fields  # pyright: ignore[reportMissingImports]


class OrderType(models.Model):
    _name = 'fixer.order.type'
    _description = 'Тип заказа-наряда'
    _order = 'name'

    name = fields.Char(string='Название', required=True)
    code = fields.Selection([
        ('installation', 'Монтаж'),
        ('repair', 'Ремонт'),
        ('refill', 'Заправка'),
        ('maintenance', 'Плановое ТО'),
        ('warranty', 'Гарантийный'),
    ], string='Код', required=True)
