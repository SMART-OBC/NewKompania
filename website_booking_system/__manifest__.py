# -*- coding: utf-8 -*-
{
  "name"                 :  "Odoo Booking & Reservation Management",
  "summary"              :  """Booking & reservation management in Odoo allows users to take appointment and ticket booking facility in Odoo website.""",
  "category"             :  "Website",
  "version"              :  "1.0.1",
  "sequence"             :  1,
  "author"               :  "SMART",
  "description"          :  """Odoo booking & reservation management
        Odoo Subscription Management
        Odoo Website Subscription Management
        Odoo appointment management
        Odoo website Appointment Management
        Schedule bookings
        Tickets
        Reservations
        Booking Facility in Odoo
        Website booking system
        Appointment management system in Odoo
        Booking & reservation management in Odoo
        Reservation management in Odoo
        Booking
        Reservation
        Booking and reservation""",

  'data' :  [
                             'security/ir.model.access.csv',
                             'views/booking_config_view.xml',
                             'views/booking_sol_view.xml',
                             'wizard/bk_qty_available_wizard_view.xml',
                             'views/product_template_view.xml',
                             'views/booking_product_cart_temp.xml',
                             'views/booking_template.xml',
                             'views/snnipets.xml',
                             'views/ir_crons.xml',
                             'views/template_address.xml',
                            ],
    'depends' :  ['website_sale','point_of_sale'],
    'qweb': [
        'static/src/xml/Chrome.xml',
        'static/src/xml/ReservationButton.xml',
        'static/src/xml/TicketScreen/TicketScreen.xml',

    ],
  'images'               :  ['static/description/Banner.png'],
  'application'          :  True,
  'installable'          :  True,
  'auto_install'         :  False,
  'pre_init_hook'        :  'pre_init_check',

}
