module.exports.PayData = Backbone.Model.extend({
    urlRoot: '/api/pay_periods_remaining',

    defaults: {
        "start_date": null,
        "frequency": "sm",
        "pay_periods_remaining": null
    }
});