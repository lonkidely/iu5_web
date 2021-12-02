export class OperCard {
    constructor(parent) {
        this.parent = parent;
    }

    getHTML(data) {
        return `
            <div class="card" style="width: 200px">
                <div class="card-body">
                    <h5 class="card-title">ID = ${data.id}</h5>
                    <p class="card-text">Обозначение:  ${data.name}</p>
                    <button class="btn btn-primary" id="click-card-${data.id}" data-id="${data.id}">Узнать количество тактов ЦП</button> 
                </div>
            </div>
        `;
    }

    addListeners(data, listener) {
        document.getElementById(`click-card-${data.id}`).addEventListener("click", listener);
    }

    render(data, listener) {
        const html = this.getHTML(data);
        this.parent.insertAdjacentHTML('beforeend', html);
        this.addListeners(data, listener)
    }
}