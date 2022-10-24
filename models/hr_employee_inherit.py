
from odoo import models, api, fields


class Hr_employee_inherit(models.Model):
    _inherit = "hr.employee"


    #agregado de campos
    uni_ope = fields.Char(string="Unidad Operativa")
    area_uniope = fields.Char(string="Area/Unidad Operativa", compute="compute_fun")

    def compute_fun(self):
        self.area_uniope =  str(self.department_id.name) + ' - ' + self.uni_ope
