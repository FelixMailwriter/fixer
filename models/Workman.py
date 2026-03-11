from odoo import models, fields # type: ignore

class Workman(models.Model):
    _name = 'fixer.workman'
    _description = 'Describe employees that can perform jobs'

    employee_id = fields.Many2one('hr.employee', string='Сотрудник', required=True)
    user_id = fields.Many2one(related='employee_id.user_id', string='Пользователь', readonly=False)
    name = fields.Char(related='employee_id.name', string='Имя', readonly=False)
    mobile_phone = fields.Char(related='employee_id.mobile_phone', string='Мобильный', readonly=False)
    work_phone = fields.Char(related='employee_id.work_phone', string='Телефон', readonly=False)
    job_title = fields.Char(related='employee_id.job_title', string='Должность', readonly=False)
    image_1920 = fields.Image(related='employee_id.image_1920', string='Фото', readonly=False)
    description = fields.Text(related='employee_id.notes',string='Описание', readonly=False)

