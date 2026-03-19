from odoo import models, fields, api  # pyright: ignore[reportMissingImports]


class Order(models.Model):
    _name = 'fixer.order'
    _description = 'Заказ-наряд'

    name = fields.Char(string='Номер заказа', required=True)
    order_type = fields.Many2one('fixer.order.type', string='Тип заказа', required=True)
    order_type_code = fields.Selection(related='order_type.code', store=False)
    client_id = fields.Many2one('res.partner', string='Клиент', required=True)
    equipment_id = fields.Many2one('fixer.equipment.card', string='Оборудование')
    user_id = fields.Many2one('res.users', string='Автор', default=lambda self: self.env.user, required=True)
    description = fields.Text(string='Примечания')

    # --- Монтаж ---
    install_track_length = fields.Float(string='Длина трассы (м)')
    install_height = fields.Float(string='Высота установки (м)')
    install_mount_type = fields.Selection([
        ('bolt', 'Болт'),
        ('clamp', 'Хомут'),
        ('profile', 'Профиль'),
        ('other', 'Другой'),
    ], string='Тип крепления')
    install_copper_pipe = fields.Float(string='Медная труба (м)')
    install_cable = fields.Float(string='Кабель (м)')
    install_fasteners = fields.Char(string='Крепёж')

    # --- Ремонт ---
    repair_symptoms = fields.Text(string='Симптомы')
    repair_diagnosis = fields.Text(string='Диагноз')
    repair_parts = fields.Text(string='Заменённые запчасти')
    repair_photo_before = fields.Image(string='Фото до')
    repair_photo_after = fields.Image(string='Фото после')

    # --- Заправка ---
    refrigerant_type = fields.Selection([
        ('r32', 'R-32'),
        ('r410a', 'R-410A'),
        ('r22', 'R-22'),
        ('r600a', 'R-600A'),
    ], string='Тип фреона')
    refrigerant_amount = fields.Float(string='Количество фреона (кг)')
    pressure_before = fields.Float(string='Давление до (бар)')
    pressure_after = fields.Float(string='Давление после (бар)')

    # --- Плановое ТО ---
    check_filters = fields.Boolean(string='Фильтры')
    check_pressure = fields.Boolean(string='Давление')
    check_electrical = fields.Boolean(string='Электрика')
    check_condensate = fields.Boolean(string='Конденсат')
    check_test = fields.Boolean(string='Тест')

    # --- Гарантийный ---
    warranty_case = fields.Char(string='Гарантийный случай')
    is_free = fields.Boolean(string='Без оплаты клиентом')

    @api.onchange('order_type')
    def _onchange_order_type(self):
        if self.order_type.code == 'warranty':
            self.is_free = True
