// Handlebars custom helpers
Handlebars.registerHelper('eachKeyValue', function(context, block) {
    return _.reduce(context, function(memo, value, key){
        return memo + block.fn({'key': key, 'value': value});
    }, "");
});