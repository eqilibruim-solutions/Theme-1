# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import odoo
from odoo import http, SUPERUSER_ID, api, tools
from odoo.http import request
import json
from odoo.addons.website_sale.controllers.main import WebsiteSale
import io
import csv
import base64
from odoo.tools import pycompat
from odoo.exceptions import UserError, AccessError, ValidationError
from psycopg2 import IntegrityError

