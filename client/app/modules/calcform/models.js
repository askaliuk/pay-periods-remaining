var Frequency = {
    DAILY: 'Daily',
    WEEKLY: 'Weekly',
    SEMI_MONTHLY: 'Semi-monthly',
    MONTHLY: 'Monthly',
    QUARTERLY: 'Quarterly'
};

var PayData = Backbone.Model.extend({
    urlRoot: '/api/pay_periods_remaining',

    defaults: {
        "start_date": null,
        "frequency": null,
        "pay_periods_remaining": null
    }
});

module.exports.PayData = PayData;
module.exports.Frequency = Frequency;