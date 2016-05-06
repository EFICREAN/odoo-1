# -*- coding: utf-8 -*-
from openerp import http

# class OpenCliente(http.Controller):
#     @http.route('/open_cliente/open_cliente/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/open_cliente/open_cliente/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('open_cliente.listing', {
#             'root': '/open_cliente/open_cliente',
#             'objects': http.request.env['open_cliente.open_cliente'].search([]),
#         })

#     @http.route('/open_cliente/open_cliente/objects/<model("open_cliente.open_cliente"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('open_cliente.object', {
#             'object': obj
#         })
