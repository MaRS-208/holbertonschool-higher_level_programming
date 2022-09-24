$.get("https://stefanbohacek.com/hellosalut/?lang=fr", function (req) { 
    $('DIV#hello').text(req.hello);
});
