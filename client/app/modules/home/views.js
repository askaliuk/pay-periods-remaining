var CalcFormView = require('modules/calcform/views'),
    template = require('./home');

var HomeView = Backbone.View.extend({
    template: template,

    render: function(){
        this.$el.html(this.template());
        var view = new CalcFormView({
            el: this.$(".ppr_form")
        });
        view.render();
        return this;
    }
});

module.exports = HomeView;