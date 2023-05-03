const header = document.querySelector('header');
const updateHeader = document.querySelector('#update_header');
updateHeader.onclick = () => {
  header.textContent = 'New Header!!!';
};
