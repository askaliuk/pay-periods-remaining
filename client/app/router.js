var HomeView = require('modules/helloworld/views');

module.exports = Backbone.Router.extend({
    routes: {
        '': 'home'
    },

    home: function() {
        $('body').html(new HomeView().render().el);
    }
});
