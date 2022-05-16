odoo.define('website_booking_system.models', function (require) {

    var models = require('point_of_sale.models');
    var rpc = require('web.rpc');
//models.load_fields('sale.order', ['name','booking_email','phone','pax','description','start','stop_time','stop','duration','type','user_id','partner_ids','code','state']);

    models.load_models([{
        model:  'sale.order',
        fields: ['name','amount_total','date_order','partner_id','state','is_booking_type'],
        domain: function(self){ return [['is_booking_type', '=', true]]; },
        loaded: function(self, reservations) {
            var reservations_ids = _.pluck(reservations, 'id');
            self.prepare_reservations_data(reservations_ids);
            self.sendMail(reservations_ids);
            self.reservations = reservations
        }
    }]);

    var _super_posmodel = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({
        initialize: function(session,attributes)
        {
            var contact_model = _.find(this.models,function(model)
            {
                return model.model === 'sale.order';
            });
            contact_model.fields.push('name','amount_total','date_order','partner_id','state','is_booking_type');
            return _super_posmodel.initialize.apply(this,arguments);
        },
        load_server_data: function () {
            var self = this;
            return _super_posmodel.load_server_data.apply(this, arguments).then(function () {
                var reservations_ids = _.map(self.reservations, function(reservations){return reservations.id;});
                return rpc.query({
                    model: 'sale.order',
                    method: 'get_whole_data',
                    args: [reservations_ids],
                });

            });
        },
        sendMail: function () {
            var self = this;
                var reservations_ids = _.map(self.reservations, function(reservations){return reservations.id;});
                return rpc.query({
                    model: 'sale.order',
                    method: 'button_sendMail_action',
                    args: [reservations_ids],
                }).catch(function (data) {
                    $(".sendMail").css("color","red").html("Failed to Sent");
                }).then(function() {
                     $(".sendMail").html("Sent Successfully");
        });

        },
        sendMail_single: function (order) {
            var self = this;
                var reservations_ids = order['id'];
                rpc.query({
                    model: 'sale.order',
                    method: 'button_sendMail_action',
                    args: [reservations_ids],
                }).catch(function (data) {
                    $('#'+order['id']).css("color","red").html("Failed to Sent");
                }).then(function(dataas) {
//                     $('#'+order['id']).html("Sent Successfully");
                        var action = {
                                    name: 'Compose Email',
                                    type: 'ir.actions.act_window',
                                    res_model: 'mail.compose.message',
                                    views: [[false, 'form']],
                                    view_mode: 'form',
                                    target: 'new',
                                    context: {
                                        default_res_id: dataas['context']['default_res_id'],
                                        default_model: dataas['context']['default_model'],
                                        default_use_template: true,
                                        default_template_id: dataas['context']['default_template_id'],
                                        force_email: true,
                                    },
                                };
                    self.do_action(dataas);
                });

        },
        prepare_reservations_data: function (data) {
            _.each(data, function (item) {
                for (var property in item) {
                    if (Object.prototype.hasOwnProperty.call(item, property)) {
                        if (item[property] === false) {
                            item[property] = " ";
                        }
                    }
                }
            });
        },
        destroy: function (){
            this.env.pos;
        },
    });
//    return models
});


