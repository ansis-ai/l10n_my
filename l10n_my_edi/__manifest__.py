###################################################################################
#
#    Copyright (C) 2024 ANSIS Pte Ltd
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

{
    "name": "Malaysia - Localization (EDI)",
    "summary": "Malaysia - Localization",
    "version": "17.0.1.0.0",
    "category": "account",
    "license": "LGPL-3",
    "author": "ANSIS",
    "maintainer": "ANSIS",
    "website": "https://ansis.com.sg/",
    "contributors": [
        "Willy <loh.wilson@gmail.com>",
    ],
    "depends": [
        "base", "account",
    ],
    "data": [
        "data/l10n_my_edi.xml",
        "views/res_config_settings_views.xml",
        "views/account_move.xml",
    ],
    "qweb": [
        # "static/src/xml/base.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'l10n_my_edi/static/src/components/*/*.js',
            'l10n_my_edi/static/src/components/*/*.xml',
            'l10n_my_edi/static/src/components/*/*.scss',
        ],
    },
    "external_dependencies": {
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
