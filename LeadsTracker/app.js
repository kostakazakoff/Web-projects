const inputEl = document.getElementById('input-field');
const inputBtn = document.getElementById('input-btn');
const tabBtn = document.getElementById('tab-btn');
const deleteBtn = document.getElementById('delete-btn');
const ulEl = document.getElementById('leads-container');
let myLeads = [];
leadsFromLocalStorage = JSON.parse(localStorage.getItem('Leads'));
console.log(leadsFromLocalStorage)

if (leadsFromLocalStorage) {
    myLeads = leadsFromLocalStorage;
    render(myLeads)
}

inputBtn.addEventListener('click', function () {
    if (inputEl.value && !myLeads.includes(inputEl.value)) {
        myLeads.push(inputEl.value);
        inputEl.value = '';
        localStorage.setItem('Leads', JSON.stringify(myLeads));
        render(myLeads);
    }
})

tabBtn.addEventListener('click', function () {
    chrome.tabs.query({
        active: true, currentWindow: true}, tabs => {
            if (!myLeads.includes(tabs[0].url)) {
                myLeads.push(tabs[0].url);
                localStorage.setItem('Leads', JSON.stringify(myLeads));
                render(myLeads);
            }
        });
});

deleteBtn.addEventListener('dblclick', function () {
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