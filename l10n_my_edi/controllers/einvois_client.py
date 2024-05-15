# -*- coding: utf-8 -*-
import base64
import contextlib
import json
import requests
import time
import logging

from datetime import datetime, timedelta

from odoo import http
from odoo.http import Controller, request, route, content_disposition


class EInvoisClient(Controller):
    """
        LHDN eInvois REST API Python Client
        Base URL for Zoom API
    """

    def __init__(self):

        super(EInvoisClient, self).__init__()

        #
        #   Retrieve 
        #
        einvois_server_base_url  = request.env["ir.config_parameter"].sudo().get_param("l10n_my_edi.einvois_server_base_url")
        einvois_client_id = request.env["ir.config_parameter"].sudo().get_param("l10n_my_edi.einvois_client_id")
        einvois_client_secret_1 = request.env["ir.config_parameter"].sudo().get_param("l10n_my_edi.einvois_client_secret_1")
        einvois_client_secret_2 = request.env["ir.config_parameter"].sudo().get_param("l10n_my_edi.einvois_client_secret_2")
        einvois_oauth_uri = f"{einvois_server_base_url}/connect/token"
        # Setup the config details
        self.config = {
            "client_id": einvois_client_id,
            "client_secret": einvois_client_secret_1,
            "base_uri": einvois_server_base_url,
            "token": self.generate_token(
                einvois_oauth_uri, einvois_client_id, einvois_client_secret_1
            ),
        }

    def refresh_token(self):
        self.config["token"] = self.generate_token(
            self.config["oauth_uri"],
            self.config["client_id"],
            self.config["client_secret"],
        )

    def generate_token(self, oauth_uri, key, secret):

        # Define the payload
        payload = {
            "client_id": key,
            "client_secret": secret,
            "grant_type": "client_credentials",
            "scope": "InvoicingAPI",
        }
        # Define the headers
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # response = requests.request("POST", url, headers=headers, data=payload)
        # Make the request
        response = requests.request('POST', oauth_uri, headers=headers, data=payload)
        token = response.json().get("access_token")
        return token

    def validate_tax_payer_TIN(self, tin, id_type, id_value):
        _uri = f"{self.config['base_uri']}/api/v1.0/taxpayer/validate/{tin}?idType={id_type}&idValue={id_value}"

        _auth_header = f"Bearer {self.config['token']}"
        headers = {
            'Authorization': _auth_header
        }
        payload = {}
        response = requests.request("GET", _uri, headers=headers, data=payload)
        print(response)    