# -*- coding: utf-8 -*-
from odoo import http

# class LibraryLoanReturnDate(http.Controller):
#     @http.route('/library_loan_return_date/library_loan_return_date/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_loan_return_date/library_loan_return_date/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_loan_return_date.listing', {
#             'root': '/library_loan_return_date/library_loan_return_date',
#             'objects': http.request.env['library_loan_return_date.library_loan_return_date'].search([]),
#         })

#     @http.route('/library_loan_return_date/library_loan_return_date/objects/<model("library_loan_return_date.library_loan_return_date"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_loan_return_date.object', {
#             'object': obj
#         })