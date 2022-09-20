$.get("https://swapi-api.hbtn.io/api/people/5/?format=json", function (req) {
  $('DIV#character').text(req.name);
});
