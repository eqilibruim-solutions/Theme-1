# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo import SUPERUSER_ID
import io
import csv
import base64
import ftplib
from odoo.tools import pycompat
from odoo.exceptions import UserError, AccessError

from odoo.addons.website_mail.models.mail_message import MailMessage
from datetime import datetime, timedelta
		
