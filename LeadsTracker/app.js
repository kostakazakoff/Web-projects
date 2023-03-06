const inputEl = document.getElementById('input-field');
const inputBtn = document.getElementById('input-btn');
const tabBtn = document.getElementById('tab-btn');
const deleteBtn = document.getElementById('delete-btn');
const ulEl = document.getElementById('leads-container');
let myLeads = [];
leadsFromLocalStorage = JSON.parse(localStorage.getItem('Leads'));
let leadsToRmv = [];
leadItems = document.getElementsByName('chkbx')


console.log(leadItems);

for(element of leadItems) {
    console.log(element)
    // leadsToRmv.push(element.childNodes);
}


// console.log(leadsToRmv)

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
        <li name="lead-item">
            <a href="${items[i]}" target="_blank">${items[i]}</a>
            <input type="checkbox" name="chkbx" id="chkbx" value="${items[i]}">
        </li>
        `;
    }
    ulEl.innerHTML = listItems;
}
