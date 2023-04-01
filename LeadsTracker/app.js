const nameInputField = document.getElementById('name-field');
const tabBtn = document.getElementById('tab-btn');
const deleteBtn = document.getElementById('delete-btn');
const ulEl = document.getElementById('leads-container');
let myLeads = [];
let leadsToRemove = [];
let leadsFromLocalStorage = JSON.parse(localStorage.getItem('Leads'));
const fragment = new DocumentFragment();

if (leadsFromLocalStorage) {
    myLeads = leadsFromLocalStorage;
    render(myLeads);
};

tabBtn.addEventListener('click', addTab);

function addTab() {
    chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
        const newTab = tabs[0].url;
        const tabExist = myLeads.filter(lead => lead.tab === newTab).length > 0;

        if (!tabExist) {
            let tab = newTab;
            let name = newTab;
            if (nameInputField.value.length > 0) {
                name = nameInputField.value;
            }
            myLeads.push({ name, tab });
            localStorage.setItem('Leads', JSON.stringify(myLeads));
            render(myLeads);
        } else {
            console.log(tabExist);
        }
    });
}

deleteBtn.addEventListener('dblclick', () => {
    localStorage.clear();
    render(leadsFromLocalStorage);
});

deleteBtn.addEventListener('click', () => {
    for (let el of leadsToRemove) {
        for (const lead of myLeads) {
            if (lead.tab === el) {
                const index = myLeads.indexOf(lead);
                myLeads.splice(index, 1);
            }
        }
    };
    localStorage.setItem('Leads', JSON.stringify(myLeads));
    render(myLeads);
});

function render(items) {
    for (let i = 0; i < items.length; i++) {
        const [name, tag] = Object.values(items[i]);
        const li = createHTMLElement('li', fragment, null, null, tag);
        createHTMLElement('a', li, name, null, null, { 'href': tag, 'target': '_blank' });
        const checker = createHTMLElement('input', li, null, ['item-checker'], null, { 'type': 'checkbox', 'name': 'item-checker', 'value': tag });
        checker.addEventListener('change', handleCheck)
    };
    ulEl.innerHTML = '';
    ulEl.appendChild(fragment);
}

function handleCheck() {
    if (this.checked) {
        console.log(this.value)
        leadsToRemove.push(this.value);
    } else {
        const index = leadsToRemove.indexOf(this.value);
        leadsToRemove.splice(index, 1);
    };
};

function createHTMLElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
    const htmlElement = document.createElement(type);

    if (content && useInnerHtml) {
        htmlElement.innerHTML = content;
    } else {
        if (content && type !== 'input') {
            htmlElement.textContent = content;
        }

        if (content && type === 'input') {
            htmlElement.value = content;
        }
    }

    if (classes && classes.length > 0) {
        htmlElement.classList.add(...classes);
    }

    if (id) {
        htmlElement.id = id;
    }

    // { src: 'link', href: 'http' }
    if (attributes) {
        for (const key in attributes) {
            htmlElement.setAttribute(key, attributes[key])
        }
    }

    if (parentNode) {
        parentNode.appendChild(htmlElement);
    }

    return htmlElement;
}