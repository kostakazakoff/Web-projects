const inputEl = document.getElementById('input-field');
const inputBtn = document.getElementById('input-btn');
const tabBtn = document.getElementById('tab-btn');
const deleteBtn = document.getElementById('delete-btn');
const ulEl = document.getElementById('leads-container');
const itemCheckers = document.getElementsByName('item-checker');
let myLeads = [];
let leadsToRemove = [];
let leadsFromLocalStorage = JSON.parse(localStorage.getItem('Leads'));

if (leadsFromLocalStorage) {
    myLeads = leadsFromLocalStorage;
    render(myLeads);
};

inputBtn.addEventListener('click', () => {
    if (inputEl.value && !myLeads.includes(inputEl.value)) {
        myLeads.push(inputEl.value);
        inputEl.value = '';
        localStorage.setItem('Leads', JSON.stringify(myLeads));
        render(myLeads);
    };
});

tabBtn.addEventListener('click', () => {
    chrome.tabs.query({active: true, currentWindow: true}, tabs => {
        if (!myLeads.includes(tabs[0].url)) {
            myLeads.push(tabs[0].url);
            localStorage.setItem('Leads', JSON.stringify(myLeads));
            render(myLeads);
        };
    });
});

deleteBtn.addEventListener('dblclick', () => {
    localStorage.clear();
    render(leadsFromLocalStorage);
});

deleteBtn.addEventListener('click', () => {
    for (el of leadsToRemove) {
        index = myLeads.indexOf(el);
        myLeads.splice(index, 1);
        localStorage.setItem('Leads', JSON.stringify(myLeads));
    };
    render(myLeads);
});

function render(items) {
    let listItems = '';
    for (let i = 0; i < items.length; i++) {
        listItems += `
        <li name="lead-item" id="${items[i]}">
            <a href="${items[i]}" target="_blank">${items[i]}</a>
            <input type="checkbox" name="item-checker" id="${items[i]}chk" value="${items[i]}">
        </li>
        `;
    };
    ulEl.innerHTML = listItems;
    listenChecks();
}

function listenChecks() {
    for (let chk in itemCheckers) {
        let checker = document.getElementById(itemCheckers[chk].id);
        if (checker) {
            checker.addEventListener('change', () => {
                if (checker.checked) {
                    leadsToRemove.push(checker.value);
                } else {
                    const index = leadsToRemove.indexOf(checker.value);
                    leadsToRemove.splice(index, 1);
                };
            });
        };
    };
};