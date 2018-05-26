# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Infor Connector Account Move",
    "summary": "",
    "version": "11.0.1.0.0",
    "license": "AGPL-3",
    "author": "Open Source Integrators, Odoo Community Association (OCA)",
    "category": "Connector",
    "website": "https://github.com/OCA/connector_infor",
    "depends": [
        "connector_infor",
        "queue_job",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/infor_backend_views.xml",
        "views/account_views.xml",
    ],
    "installable": True,
}