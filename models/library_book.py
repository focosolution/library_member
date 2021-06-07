from odoo import api, fields, models


class Book(models.Model):
    _inherit = 'library.book'
    is_available = fields.Boolean('Is Available?')

    # Os campos abaixo já existiam e foram modificados. Para isso foi utilizado o mesmo tipo e adicionando 
    # num caso o help e no outro a indexação. O restante permanece inalterado.
    isbn = fields.Char(help="Use a valid ISBN-13 or ISBN-10.")
    publisher_id = fields.Many2one(index=True)
