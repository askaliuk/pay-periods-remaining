// Handlebars custom helpers
Handlebars.registerHelper('eachKeyValue', function(context, block) {
    return _.reduce(context, function(memo, value, key){
        return memo + block.fn({'key': key, 'value': value});
    }, "");
});

/**
* Show 'selected' if
* {{#selected_if x compare=y}}
*/
Handlebars.registerHelper('selected_if', function(context, options) {
    if (context == options.hash.compare) {
        return "selected";
    }
    return "";
});