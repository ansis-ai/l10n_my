# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, RedirectWarning, ValidationError
from odoo import models, fields, api, _
from ..controllers.einvois_client import EInvoisClient

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = "account.move"

    einvois_state = fields.Selection(
        string=_('eInvois Status'),
        selection=[
            ('draft', 'Not Ready'),
            ('ready', 'Ready'),
            ('submit', 'Submitted'),
        ],
    )

    def action_einvois_submit(self):
        for record in self:
            print(f"SEND TO E-INVOICE")
            _client = EInvoisClient()
            _tin = 'PT24905762100'
            _id_type = 'BRN'
            _id_value = '201604001399'
            _client.validate_tax_payer_TIN(_tin, _id_type, _id_value)

