from odoo import models, fields

class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student"

    name = fields.Char(string="Name", required=True)
    roll_number = fields.Char(string="Roll Number", required=True)
    class_name = fields.Char(string="Class")
    age = fields.Integer(string="Age")
    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
            ('common', 'Common'),
            ('others', 'Others'),
        ],
        string="Gender",
    )
