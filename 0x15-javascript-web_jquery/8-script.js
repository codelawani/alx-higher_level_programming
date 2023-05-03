const moviesList = document.getElementById('list_movies');
fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    for (const result of data.results) {
      const list = document.createElement('li');
      list.textContent = result.title;
      moviesList.append(list);
    }
  })
  .catch((err) => console.log(err));
