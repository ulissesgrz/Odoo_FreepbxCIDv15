# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.http import request, Response

import json


class PartnerConsultController(http.Controller):

    @http.route('/consp', auth='public', type='http', methods=['GET'], website=True)
    def partnerconsult(self, **kwargs):
        number = kwargs.get('number')
        apikey = kwargs.get('apikey')
        apikey_parm = request.env['ir.config_parameter'].sudo().get_param('partner_consult_custom.apikey')
        if not number or not apikey or not apikey_parm:
            return Response(' ', content_type='text/html;charset=utf-8', status=500)
        if apikey_parm != apikey:
            return Response(' ', content_type='text/html;charset=utf-8', status=500)
        number = number.replace(' ', '').replace('+', '')
        partners = request.env['res.partner'].sudo().search(['|', ('phone', '!=', False), ('mobile', '!=', False)])
        for partner in partners:
            number = number.replace(' ', '').replace('+', '').replace('-', '')
            partner_search = False
            if partner.mobile and partner.mobile.replace(' ', '').replace('+', '').replace('-', '') == number:
                partner_search = True
            if partner.phone and partner.phone.replace(' ', '').replace('+', '').replace('-', '') == number:
                partner_search = True
            if partner_search:
                #values = {
                #    'partner': partner
                #}
                headers = {'Content-Type': 'application/json'}
                body = {'results': partner.name}
                return Response(partner.name, content_type='text/html;charset=utf-8', status=500)
                #return Response(json.dumps(body), headers=headers)
                #return request.render("partner_consult_custom.partner_consult_page", values)
        return Response('*' + number, content_type='text/html;charset=utf-8', status=500)

