var PayData = require('./models').PayData,
    Frequency = require('./models').Frequency,
    template = require('./calcform');


var CalcFormView = Backbone.View.extend({
    template: template,

    events: {
      'click .calculate' : 'calculate',
      'click .start_date_today' : 'onTodayClick'
    },

    initialize: function(){
        this.model = new PayData();
        this.error = null;
        _.bindAll(this);
    },

    calculate: function(){
        this.model.set('pay_periods_remaining', null);
        this.model.set('start_date', this.$('.start_date').val());
        this.model.set('frequency', this.$('.frequency').val());
        this.error = null;
        this.model.fetch({
            data: this.model.toJSON(),
            success: this.render,
            error: this.onError
        });
    },

    getToday: function(){
        var today = new Date();
        var dd = today.getDate();
        var mm = today.getMonth()+1; // January is 0!
        var yyyy = today.getFullYear();
        if (dd < 10) {dd = '0' + dd;}
        if (mm < 10) {mm = '0' + mm;}
        today = mm + '/' + dd + '/' + yyyy;
        return today;
    },

    onTodayClick: function() {
        this.model.set('start_date', this.getToday());
        this.render();
    },

    onError: function(model, response, options) {
        if (response.status === 400) {
            this.error = $.parseJSON(response.responseText).message;
        } else {
            this.error = response.statusText;
        }
        this.render();
    },

    render: function(){
        var context = {
            frequency: Frequency,
            pay_data: this.model.attributes,
            error: this.error
        };
        this.$el.html(this.template(context));
        this.trigger("render:finished"); // for tests
        return this;
    }
});

module.exports = CalcFormView;