odoo.define("rental_ecommerce.tour_shop_frontend", function (require) {
"use strict";

var tour = require("web_tour.tour");
var steps = require("rental_ecommerce.tour_shop");
tour.register("shop", {
    url: "/rent",
}, steps);

});
