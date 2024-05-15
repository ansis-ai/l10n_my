# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, fields, models


class l10n_my_ediConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    einvois_server_base_url = fields.Char(string=_('einvois_client_id'), config_parameter='l10n_my_edi.einvois_server_base_url')
    einvois_client_id = fields.Char(string=_('LHDN '), config_parameter='l10n_my_edi.einvois_client_id')
    einvois_client_secret_1 = fields.Char(string=_('LHDN eInvois Client Secret 1'), config_parameter='l10n_my_edi.einvois_client_secret_1')
    einvois_client_secret_2 = fields.Char(string=_('LHDN eInvois Client Secret 2'), config_parameter='l10n_my_edi.einvois_client_secret_2')
