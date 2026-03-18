from odoo import models, fields, api  # pyright: ignore[reportMissingImports]
from datetime import date, timedelta


class EquipmentCard(models.Model):
    _name = 'fixer.equipment.card'
    _description = 'Карточка оборудования'
    _order = 'brand, model_id'

    brand = fields.Many2one('fixer.brand', string='Бренд', required=True)

    model_id = fields.Many2one('fixer.equipment.model', string='Модель оборудования', required=True)
    serial_number = fields.Char(string='Серийный номер')
    site_id = fields.Many2one('res.partner', string='Объект установки')

    install_date = fields.Date(string='Дата монтажа')
    warranty_end = fields.Date(string='Дата окончания гарантии')
    warranty_status = fields.Selection([
        ('active', 'Активна'),
        ('expiring', 'Истекает'),
        ('expired', 'Истекла'),
    ], string='Статус гарантии', compute='_compute_warranty_status')

    refrigerant_type = fields.Selection([
        ('r32', 'R-32'),
        ('r410a', 'R-410A'),
        ('r22', 'R-22'),
        ('r600a', 'R-600A'),
    ], string='Тип хладагента')
    refrigerant_amount = fields.Float(string='Объём заправки (кг)')

    last_service_date = fields.Date(string='Дата последнего ТО')
    next_service_date = fields.Date(string='Плановая дата следующего ТО')

    order_ids = fields.One2many('fixer.order', 'equipment_id', string='Заказы-наряды')

    @api.depends('warranty_end')
    def _compute_warranty_status(self):
        today = date.today()
        for rec in self:
            if not rec.warranty_end:
                rec.warranty_status = False
            elif rec.warranty_end <= today:
                rec.warranty_status = 'expired'
            elif rec.warranty_end <= today + timedelta(days=30):
                rec.warranty_status = 'expiring'
            else:
                rec.warranty_status = 'active'
