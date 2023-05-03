// Get the classList of the header element
const headerClasses = document.querySelector('header').classList;
// Get the header color toggler
const redHeader = document.querySelector('#toggle_header');
redHeader.onclick = () => {
  // Toggle the 'red' and 'green' classes on the header element
  headerClasses.toggle('red');
  headerClasses.toggle('green');
};
