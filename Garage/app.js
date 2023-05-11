const BASE_URL = 'https://api.sheety.co/d9720f78f21726e71b7382e3cab36f43/garage'

function start() {
    const garageMenu = document.getElementById('garageMenu');
    const garage = document.getElementById('garage');
    const vehicleList = document.getElementById('vehicle-service');
    const home = document.getElementById('home');
    const nav = document.getElementById('nav')
    let caschedData = [];
    home.addEventListener('click', loadAllVehicles)
    loadAllVehicles();

    function loadAllVehicles() {
        garage.innerHTML = '';
        vehicleList.innerHTML = '';
        garage.classList = ['section-flex'];
        fetch(`${BASE_URL}/vehicleItems`)
            .then(res => res.json())
            .then(data => handleData(data))
            .catch(err => console.error(err));
    }

    function handleData(data) {
        garageMenu.innerHTML = '';
        const vehicleList = createHTMLElement('ul', garageMenu, null, null, null, { 'role': 'list' });

        if (data.vehicleItems.length < 4) {
            const addNewVehicle = createHTMLElement('li', nav, 'Add New Vehicle', ['nav__item', 'right-nav-item']);
            addNewVehicle.addEventListener('click', addNewVehicle)
        }

        Object.values(data.vehicleItems).forEach(v => {
            caschedData.push(v);
            const menuVehicle = createHTMLElement('li', vehicleList, v.brand, ['nav__rolldown__item']);
            menuVehicle.addEventListener('click', loadVehicleService);
            const vehicle = createHTMLElement('article', garage, null, ['vehicle'], v.id - 1);
            const params = createHTMLElement('div', vehicle, null, ['vehicle', 'params'])
            createHTMLElement('p', params, `${v.brand}`, ['vehicle__brand']);
            createHTMLElement('p', params, `Model: ${v.model}`, ['vehicle__model']);
            createHTMLElement('p', params, `VIN: ${v.vin}`, ['vehicle__vin']);
            createHTMLElement('p', params, `Plate: ${v.plate}`, ['vehicle__plate']);
            createHTMLElement('p', params, `Odometer: ${v.odometer}`, ['vehicle__odometer']);
            createHTMLElement('p', params, `Year: ${v.year}`, ['vehicle__year']);

            params.addEventListener('click', loadVehicleService)

            const btnsContainer = createHTMLElement('div', vehicle, null, ['btns-container']);
            const vehicleEditBtn = createHTMLElement('button', btnsContainer, 'Edit', ['btn', 'primary-btn']);
            vehicleEditBtn.addEventListener('click', editVehicle);
            const vehicleDeleteBtn = createHTMLElement('button', btnsContainer, 'Delete', ['btn', 'danger-btn']);
            vehicleDeleteBtn.addEventListener('click', deleteVehicle);
        });
    }

    function loadVehicleService() {
        const id = this.id;
        const model = this.querySelector('.vehicle__brand').textContent
        this.parentNode.classList = ['hidden'];
        vehicleList.classList = ['section-flex'];

        fetch(`${BASE_URL}/${id}`)
            .then(res => res.json())
            .then(data => outputService(Object.values(data[id]), id, model))
            .catch(err => console.error(err));
    }

    function outputService(data, id, model) {
        console.log(data);

        createHTMLElement('h2', vehicleList, `${model} Service History`, ['section-title'], id)
        for (let i = 0; i < data.length; i++) {
            
            // const form = createHTMLElement('form', vehicleList, null, ['service-item'], i);
            // createHTMLElement('input', form, null, null, 'description', { 'value': data[i].description });
            // const odometer = createHTMLElement('div', form, null, ['service-item__row'])
            // createHTMLElement('label', odometer, 'Odometer');
            // createHTMLElement('input', odometer, null, null, 'km', { 'value': data[i].km });
            // const date = createHTMLElement('div', form, null, ['service-item__row'])
            // createHTMLElement('label', date, 'Date');
            // createHTMLElement('input', date, null, null, 'date', { 'value': data[i].date });

            const article = createHTMLElement('article', vehicleList, null, ['vehicle', 'service-item']);
            createHTMLElement('h3', article, data[i].description, ['service-item__row']);
            createHTMLElement('div', article, `Odometer: ${data[i].odometer}`, ['service-item__row']);
            createHTMLElement('div', article, `Date: ${data[i].date}`, ['service-item__row']);
            createHTMLElement('div', article, `Notes: ${data[i].notes}`, ['service-item__row']);
            createHTMLElement('div', article, `Autoservice: ${data[i].service}`, ['service-item__row']);
            createHTMLElement('div', article, `Price: ${data[i].price}`, ['service-item__row']);

            const btnsContainer = createHTMLElement('div', article, null, ['btns-container']);
            const vehicleEditBtn = createHTMLElement('button', btnsContainer, 'Edit', ['btn', 'primary-btn']);
            vehicleEditBtn.addEventListener('click', editServiceItem);
            const vehicleDeleteBtn = createHTMLElement('button', btnsContainer, 'Delete', ['btn', 'danger-btn']);
            vehicleDeleteBtn.addEventListener('click', deleteServiceItem);
        }
    }

    function editServiceItem() {
        // TODO
    }

    function deleteServiceItem() {
        // TODO
    }

    function editVehicle() {
        const vehicle = this.parentNode.parentNode;
        const id = parseInt(this.parentNode.parentNode.id) + 1;
        console.log(id)
        const v = caschedData.find((obj) => obj.id == id);
        console.log(caschedData);
        this.parentNode.parentNode.innerHTML = '';

        const brand = createHTMLElement('input', vehicle, null, ['vehicle__brand'], null, { 'type': 'text', 'value': v.brand });
        const model = createHTMLElement('input', vehicle, null, ['vehicle__model'], null, { 'type': 'text', 'value': v.model });
        const vin = createHTMLElement('input', vehicle, null, ['vehicle__vin'], null, { 'type': 'text', 'value': v.vin });
        const plate = createHTMLElement('input', vehicle, null, ['vehicle__plate'], null, { 'type': 'text', 'value': v.plate });
        const odometer = createHTMLElement('input', vehicle, null, ['vehicle__odometer'], null, { 'type': 'number', 'value': v.odometer });
        const year = createHTMLElement('input', vehicle, null, ['vehicle__year'], null, { 'type': 'text', 'value': v.year });

        const btnsContainer = createHTMLElement('div', vehicle, null, ['btns-container']);
        const saveBtn = createHTMLElement('button', btnsContainer, 'Save', ['btn', 'primary-btn']);
        const cancelBtn = createHTMLElement('button', btnsContainer, 'Cancel', ['btn', 'danger-btn']);
        cancelBtn.addEventListener('click', () => loadAllVehicles())

        saveBtn.addEventListener('click', () => {
            const editedVehicle = {
                'vehicleItem': {
                    "id": id,
                    "brand": brand.value,
                    "model": model.value,
                    "vin": vin.value,
                    "plate": plate.value,
                    "odometer": odometer.value,
                    "year": year.value
                }
            }

            const putHeaders = {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(editedVehicle)
            }
            fetch(`${BASE_URL}/vehicleItems/${id}`, putHeaders)
                .then(loadAllVehicles)
                .catch(err => console.error(err));
        })
    }

    function deleteVehicle() {
        const id = parseInt(this.parentNode.parentNode.id) + 1;

        const deleteHeaders = {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
        }
        // fetch(`${BASE_URL}/${id}`, deleteHeaders)
        //     .then(
        fetch(`${BASE_URL}/vehicleItems/${id}`, deleteHeaders)
            .then(loadAllVehicles)
            .catch(err => console.error(err))
        // )
        // .catch(err => console.error(err))
    }

    function addNewVehicle() {
        console.log(this);
    }

}

start();

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