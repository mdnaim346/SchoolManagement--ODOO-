from odoo import models, fields

class SchoolStudent(models.Model):
    _name = "school.teacher"
    _description = "School Teacher"

    name = fields.Char(string="Name", required=True)
    employee_id =fields.Integer(string='Employee Id' , required=True)
    course = fields.Many2many('school.course', string='courses')
    
