var PayData = require('./models').PayData,
    template = require('./templates/home');

var HomeView = Backbone.View.extend({
    template: template,

    render: function(){
        this.$el.html(this.template());
        var view = new CalcFormView({
            el: this.$el.find(".ppr_form")
        });
        view.render();
        return this;
    }
});

var CalcFormView = Backbone.View.extend({

    events: {
      "click .calculate" : "calculate",
      "click .start_date_today" : "setToday"
    },

    initialize: function(){
        this.model = new PayData();
        this.listenTo(this.model, "change", this.render);
        // TODO(askalyuk): refactor this to function with cache
        this.$ppr_result = this.$el.find('.ppr_result');
        this.$ppr_alert = this.$el.find('.ppr_alert');
        this.$ppr_error = this.$el.find('.ppr_error');
        this.$start_date = this.$el.find('input[name=start_date]');
        this.$frequency= this.$el.find('select[name=pay_frequency]');
        _.bindAll(this);
    },

    calculate: function(){
        this.$ppr_error.hide();
        this.model.set("start_date", this.$start_date.val());
        this.model.set("frequency", this.$frequency.val());
        this.model.fetch({
            data: this.model.toJSON(),
            error: this.modelError
        });
    },

    setToday: function() {
        var today = new Date();
        var dd = today.getDate();
        var mm = today.getMonth()+1; // January is 0!
        var yyyy = today.getFullYear();
        if (dd < 10) {dd = '0' + dd;}
        if (mm < 10) {mm = '0' + mm;}
        today = mm + '/' + dd + '/' + yyyy;
        this.$start_date.val(today);
    },

    modelError: function(model, response, options) {
        if (response.status === 400) {
            message = $.parseJSON(response.responseText).message;
            this.$ppr_error.html(message).show();
        } else {
            this.$ppr_error.html(response.statusText).show();
        }
    },

    render: function(){
        console.log("render");
        this.$ppr_error.hide();
        var ppr = this.model.get('pay_periods_remaining');
        if (_.isNull(ppr)) {
            this.$ppr_alert.hide();
        } else {
            this.$ppr_result.html(ppr);
            this.$ppr_alert.show();
            this.$ppr_error.hide();
        }
        return this;
    }
});

module.exports = HomeView;