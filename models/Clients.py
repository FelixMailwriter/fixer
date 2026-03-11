from odoo import models, fields # type: ignore

class Clients(models.Model):
    _name = 'fixer.client'
    _description = 'Describe clients'

    client_id = fields.Many2one('res.partner', string='Клиент', domain=[('customer_rank', '>', 0)], required=True)

    name = fields.Char(related='client_id.name', string='Name', readonly=False)
    phone = fields.Char(related='client_id.phone', string='Телефон', readonly=False)
    mobile = fields.Char(related='client_id.mobile', string='Мобильный', readonly=False)
    email = fields.Char(related='client_id.email', string='Email', readonly=False)
    is_company = fields.Boolean(related='client_id.is_company', string='Компания', readonly=False)
    vat = fields.Char(related='client_id.vat', string='ИНН', readonly=False)
    street = fields.Char(related='client_id.street', string='Улица', readonly=False)
    city = fields.Char(related='client_id.city', string='Город', readonly=False)
    zip = fields.Char(related='client_id.zip', string='Почтовый индекс', readonly=False)
    country_id = fields.Many2one(related='client_id.country_id', string='Страна', readonly=False)
    description = fields.Html(string='Описание', related='client_id.comment', readonly=False)

