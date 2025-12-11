from odoo import models, fields

class SchoolStudent(models.Model):
    _name = "school.course"
    _description = "School Course"

    name = fields.Char(string="Name", required=True)
    duration=fields.Integer(string="Duration")
    
