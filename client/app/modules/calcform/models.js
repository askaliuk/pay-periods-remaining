var Frequency = {
	// TODO(askalyuk): implement others
    SEMI_MONTHLY : {value: 'sm', name: 'Semi-monthly'}
};

var PayData = Backbone.Model.extend({
    urlRoot: '/api/pay_periods_remaining',

    defaults: {
        "start_date": null,
        "frequency": Frequency.SEMI_MONTHLY,
        "pay_periods_remaining": null
    }
});

module.exports.PayData = PayData;
module.exports.Frequency = Frequency;