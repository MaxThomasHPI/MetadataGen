import {buildRow, buildInput} from "../helper.js";
import {buildBaseInput} from "./baseInputTemplate.js";

const template = [
        {"id": "general-name", "label": "Name", "type": "tf", "mandatory": true, "test": false},
        {"id": "general-description", "label": "Description", "type": "ta", "mandatory": true, "test": false},
        {"id": "general-url", "label": "Course URL/URI", "type": "tf", "mandatory": true, "test": "url"},
        {"id": "general-startDate", "label": "Start Date", "type": "tf", "mandatory": false, "test": "date"},
        {"id": "general-endDate", "label": "End Date", "type": "tf", "mandatory": false, "test": "date"},
];


export function buildGeneralUi() {
    const container = document.getElementById("general-container");
    buildBaseInput(container, template);
    /**
    for (const field of template){
        const id = field["id"];
        const label = field["label"];
        const type = field["type"];
        const mandatory = field["mandatory"];

        const input = buildInput(type, id);
        container.appendChild(buildRow(input, label, mandatory));
    }**/
}


export function getTemplate() {
    return template;
}