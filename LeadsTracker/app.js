const inputEl = document.getElementById('input-field');
const saveInputBtn = document.getElementById('save-input');
const saveTagBtn = document.getElementById('save-tag');
const deleteBtn = document.getElementById('delete');
const ulEl = document.getElementById('leads-container');
let myLeads = [];
leadsFromLocalStorage = JSON.parse(localStorage.getItem('Leads'));
console.log(leadsFromLocalStorage)

if (leadsFromLocalStorage) {
    myLeads = leadsFromLocalStorage;
    render(myLeads)
}

saveInputBtn.addEventListener('click', function() {
    if (inputEl.value && !myLeads.includes(inputEl.value)) {
        myLeads.push(inputEl.value);
        inputEl.value = '';
    localStorage.setItem('Leads', JSON.stringify(myLeads));
    render(myLeads);
    }
})

deleteBtn.addEventListener('click', function() {
    localStorage.clear()
    render(myLeads)
})

function render(items) {
    let listItems = '';
    for (let i = 0; i < items.length; i++) {
        listItems += `
        <li>
            <a href="${items[i]}" target="_blank">${items[i]}</a>
        </li>   
        `;
    }
    console.log(listItems);
    ulEl.innerHTML = listItems;
}