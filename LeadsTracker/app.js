const inputEl = document.getElementById('input-field');
const inputBtn = document.getElementById('input-btn');
const tabBtn = document.getElementById('tab-btn');
const deleteBtn = document.getElementById('delete-btn');
const ulEl = document.getElementById('leads-container');
let myLeads = [];
leadsFromLocalStorage = JSON.parse(localStorage.getItem('Leads'));

if (leadsFromLocalStorage) {
    myLeads = leadsFromLocalStorage;
    render(myLeads)
}

inputBtn.addEventListener('click', () => {
    if (inputEl.value && !myLeads.includes(inputEl.value)) {
        myLeads.push(inputEl.value);
        inputEl.value = '';
        localStorage.setItem('Leads', JSON.stringify(myLeads));
        render(myLeads);
    }
})

tabBtn.addEventListener('click', () => {
    chrome.tabs.query({
        active: true, currentWindow: true
    }, tabs => {
        if (!myLeads.includes(tabs[0].url)) {
            myLeads.push(tabs[0].url);
            localStorage.setItem('Leads', JSON.stringify(myLeads));
            render(myLeads);
        }
    });
});

deleteBtn.addEventListener('dblclick', () => {
    localStorage.clear();
    render(myLeads);
});

function render(items) {
    let listItems = '';
    for (let i = 0; i < items.length; i++) {
        listItems += `
        <li>
            <a href="${items[i]}" target="_blank">${items[i]}</a>
            <button class="chkbx-rmv-btn" name="chkbx-rmv-btn" id="chkbx-rmv-btn" value="${items[i]}"><i class="fa-solid fa-xmark"></i></button>
        </li>
        `;
    }
    ulEl.innerHTML = listItems;
}
