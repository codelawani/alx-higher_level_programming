const hello = document.getElementById('hello');
fetch('https://fourtonfish.com/hellosalut/?lang=fr')
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
  })
  .catch((err) => console.log(err));
