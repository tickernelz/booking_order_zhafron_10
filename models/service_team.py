from odoo import fields, models, api


class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'service time'

    name = fields.Char(string='Team Name', required=True)
    team_leader = fields.Many2one('res.users', string='Team Leader', required=True)
    team_members = fields.Many2many('res.users', string='Team Members')
