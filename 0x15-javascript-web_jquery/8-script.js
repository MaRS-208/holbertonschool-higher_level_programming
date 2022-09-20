$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (chr) {
  for (let index in chr.results) {
    $('UL#list_movies').append('<li>' + chr.results[index].title + '</li>');
  }
});
