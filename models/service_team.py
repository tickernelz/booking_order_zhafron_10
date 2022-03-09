import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, exceptions, _
from odoo.osv import osv
import logging
_logger = logging.getLogger(__name__)


class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'service time'

    name = fields.Char(string='Team Name', required=True)
    team_leader = fields.Many2one('res.users', string='Team Leader', required=True)
    team_members = fields.Many2many('res.users', string='Team Members')
