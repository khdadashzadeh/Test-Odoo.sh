# -*- coding: utf-8 -*-
from odoo.exceptions import UserError
from odoo import fields,_
from odoo.osv import osv
from odoo import api, fields, models, _

class AccountPaymentExtension(models.Model):
    _inherit='res.partner'

    test1000 =fields.Char('Test 1000')