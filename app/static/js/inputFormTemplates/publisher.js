import {buildInput, buildRow} from "../helper.js";

const template = [
    {"id": "publisher-name", "label": "Name", "type": "tf", "mandatory": true, "test": false},
    {"id": "publisher-url", "label": "Homepage", "type": "tf", "mandatory": false, "test": "url"},
    {"id": "publisher-description", "label": "Description", "type": "ta", "mandatory": false, "test": false}
];


export function buildPublisherUi() {
    const container = document.getElementById("publisher-container");

    for (const field of template){
        const id = field["id"];
        const label = field["label"];
        const type = field["type"];
        const mandatory = field["mandatory"];

        const input = buildInput(type, id);
        container.appendChild(buildRow(input, label, mandatory));
    }
}


export function getTemplate() {
    return template;
}