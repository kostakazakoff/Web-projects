const BASE_URL = 'https://api.sheety.co/d9720f78f21726e71b7382e3cab36f43/garage'

function start() {
    const garageMenu = document.getElementById('garageMenu');
    const garage = document.getElementById('garage');
    const vehicleList = document.getElementById('vehicle-service');
    // const service = document.getElementById('service');
    const reminders = document.getElementById('reminders');
    let caschedData = [];
    loadAllVehicles();

    function loadAllVehicles() {
        garage.innerHTML = '';
        garage.classList = ['section-flex'];
        fetch(`${BASE_URL}/vehicleItems`)
            .then(res => res.json())
            .then(data => handleData(data))
            .catch(err => console.error(err));
    }

    function handleData(data) {
        const vehicleList = createHTMLElement('ul', garageMenu, null, null, null, { 'role': 'list' });

        Object.values(data.vehicleItems).forEach(v => {
            caschedData.push(v);
            const menuVehicle = createHTMLElement('li', vehicleList, v.brand, ['nav__rolldown__item']);
            menuVehicle.addEventListener('click', loadVehicleService);
            const vehicle = createHTMLElement('article', garage, null, ['vehicle'], v.id-1);
            createHTMLElement('p', vehicle, `${v.brand}`, ['vehicle__brand']);
            createHTMLElement('p', vehicle, `Model: ${v.model}`, ['vehicle__model']);
            createHTMLElement('p', vehicle, `VIN: ${v.vin}`, ['vehicle__vin']);
            createHTMLElement('p', vehicle, `Plate: ${v.plate}`, ['vehicle__plate']);
            createHTMLElement('p', vehicle, `Odometer: ${v.odometer}`, ['vehicle__odometer']);
            createHTMLElement('p', vehicle, `Year: ${v.year}`, ['vehicle__year']);

            const btnsContainer = createHTMLElement('div', vehicle, null, ['btns-container']);
            const vehicleEditBtn = createHTMLElement('button', btnsContainer, 'Edit', ['btn', 'primary-btn']);
            vehicleEditBtn.addEventListener('click', editVehicle);
            const vehicleDeleteBtn = createHTMLElement('button', btnsContainer, 'Delete', ['btn', 'danger-btn']);
            vehicleDeleteBtn.addEventListener('click', deleteVehicle);

            vehicle.addEventListener('click', loadVehicleService)
        });

        const addNewVehicleItem = createHTMLElement('p', vehicleList, 'Add New Vehicle', ['nav__rolldown__item']);
        addNewVehicleItem.addEventListener('click', addNewVehicle)
    }

    function loadVehicleService() {
        const id = this.id;
        this.parentNode.classList = ['hidden'];
        vehicleList.classList = ['section-flex'];

        fetch(`${BASE_URL}/${id}`)
            .then(res => res.json())
            .then(data => outputService(Object.values(data[id])))
            .catch(err => console.error(err));
    }

    function outputService(data) {
        console.log(data);

        // const tbody = createHTMLElement('tbody', table);
        const service = createHTMLElement('article', vehicleList)
        for (let i = 0; i < data.length; i++) {
            const form = createHTMLElement('form', service, null, ['vehicle-row'], i);
            createHTMLElement('label', form, 'Description');
            createHTMLElement('input', form, null, null, 'description', { 'value': data[i].description });
            createHTMLElement('label', form, 'Odometer');
            createHTMLElement('input', form, null, null, 'km', { 'value': data[i].km });
            createHTMLElement('label', form, 'Date');
            createHTMLElement('input', form, null, null, 'date', { 'value': data[i].date });
            // TODO: service row items
        }
    }

    function editVehicle() {
        const vehicle = this.parentNode.parentNode;
        const id = parseInt(this.parentNode.parentNode.id);
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
        const id = this.parentNode.parentNode.id;
        const deleteHeaders = {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
        }
        fetch(`${BASE_URL}/${id}`, deleteHeaders)
            .then(
                fetch(`${BASE_URL}/vehicleItems/${id}`, deleteHeaders)
                    .then(loadAllVehicles)
                    .catch(err => console.error(err))
            )
            .catch(err => console.error(err))
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