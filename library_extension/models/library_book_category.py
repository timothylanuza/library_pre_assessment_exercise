from odoo import models, fields, api
from odoo.exceptions import UserError

class LibraryBookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Book Category'

    name = fields.Char(string='Category Name', required=True)
    
    @api.constrains('name')
    def _check_name_unique(self):
        for rec in self:
            existing = self.search([
                ('name', '=', rec.name),
                ('id', '!=', rec.id)
            ], limit=1)
            if existing:
                rec.name = False
                raise UserError("Category name must be unique.")
