odoo.define('website_booking_system.ReservationButton', function (require) {
    'use strict';
//http://localhost:1414/pos/ui?debug=assets&config_id=1#cids=1
    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const { posbus } = require('point_of_sale.utils');

    class ReservationButton extends PosComponent {
        onClick() {
            if (this.props.isReservationTicketScreenShown) {
                posbus.trigger('ticket-button-clicked');
            } else {
                this.showScreen('ReservationTicketScreen');
            }
        }
        willPatch() {
            posbus.off('order-deleted', this);
        }
        patched() {
            posbus.on('order-deleted', this, this.render);
        }
        mounted() {
            posbus.on('order-deleted', this, this.render);
        }
        willUnmount() {
            posbus.off('order-deleted', this);
        }
        get count() {
            if (this.env.pos.reservations) {
                return this.env.pos.reservations.length;
            } else {
                return 0;
            }
        }
    }
    ReservationButton.template = 'ReservationButton';

    Registries.Component.add(ReservationButton);

    return ReservationButton;
});
