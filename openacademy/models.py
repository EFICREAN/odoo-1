# -*- coding: utf-8 -*-

from openerp import models, fields, api

class openacademy_course(models.Model):
	_name = 'openacademy.course'
	name = fields.Char(string="Title", required=True)
	description = fields.Text(string="Description")
	responsible_id = fields.Many2one('res.users',ondelete='set null', string="Responsible", index = True)
	session_ids = fields.One2many('openacademy.session','course_id',string="session")
class openacademy_session(models.Model):
	_name = 'openacademy.session'
	name=fields.Char(string="Session Title", size=128, required=True)
	start_date = fields.Date(string='Start Date')
	duration = fields.Float(string='Duration',digits=(6,2),help="Duration in Hours")
	seats = fields.Integer(string="Seat Number")
	instructor_id = fields.Many2one('res.partner',string="Instructor")
	course_id=fields.Many2one('openacademy.course',ondelete='cascade',string="Course",required=True)
	attendee_ids = fields.One2many('openacademy.attendee','session_id',string="Attendees")
        attendee_ids2= fields.Many2many('res.partner',string="Attendees2") 

class openacademy_attendee(models.Model):
    _name = 'openacademy.attendee'
    name = fields.Char(string="Attendee", size=64)
    session_id = fields.Many2one('openacademy.session', string="Session")
    partner_id = fields.Many2one('res.partner', string="Partner")
