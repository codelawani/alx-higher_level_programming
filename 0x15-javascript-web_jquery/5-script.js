const myList = document.querySelector('UL.my_list');
const itemAdder = document.querySelector('#add_item');
itemAdder.onclick = () => {
  const listItem = document.createElement('li');
  listItem.textContent = 'Item';
  myList.appendChild(listItem);
};
