var CalcFormView = require('modules/calcform/views');

suite('CalcForm', function(){
  suite('views', function(){

    setup(function(){
        this.view = new CalcFormView();
        assert.ok(this.view.template);
        this.view.render();
        assert.ok(this.view.el);
    });

    teardown(function(){
        this.view.remove();
    });

    test('init', function(){
        assert.isFalse(this.view.$(".alert-error").exists(),
            "error is visible");
        assert.isFalse(this.view.$(".alert-success").exists(),
            "result is visible");
    });

    test('onTodayClick', function(done){
        this.view.once("render:finished", function(){
            assert.equal(this.view.$(".start_date").val(),
                this.view.getToday());
            done();
        }, this);
        this.view.$(".start_date_today").trigger("click");
    });

  });
});