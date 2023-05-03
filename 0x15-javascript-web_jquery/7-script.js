const character = document.getElementById('character');
fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .then((response) => response.json())
  .then((data) => {
    character.textContent = data.name;
  })
  .catch((err) => console.log(err));
