var PayData = require('./models').PayData,
    template = require('./templates/home');

var HomeView = Backbone.View.extend({
    template: template,

    render: function(){
        this.$el.html(this.template());
        var view = new CalcFormView({
            el: this.$el.find("#ppr_form")
        });
        return this;
    }
});

var CalcFormView = Backbone.View.extend({

    events: {
      "click #calculate" : "calculate"
    },

    initialize: function(){
        this.model = new PayData();
        this.listenTo(this.model, "change", this.render);
    },

    calculate: function(){
        // TODO(askalyuk): implement validation
        this.model.fetch();
    },

    render: function(){
        console.log(this.model.get('pay_periods_remaining'));
        // TODO(askalyuk): implement results render
        return this;
    }
});

module.exports = HomeView;