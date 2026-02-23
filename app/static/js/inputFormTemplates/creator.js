import {buildAddAndDeleteButton, buildInput, buildRow} from "../helper.js";

const template = [  // Make Map and "id" as key! Introduce "attributeName" for collecting and saving in raw data!
    {"id": "creator-name", "label": "Name", "type": "tf", "mandatory": true, "test": false},
    {"id": "creator-honorificPrefix", "label": "Honorific Prefix (Dr., Prof., ...", "type": "tf", "mandatory": false, "test": false},
    {"id": "creator-description", "label": "Description", "type": "ta", "mandatory": false, "test": false}
];


export function buildCreatorUi(isFirst = true) {
    const container = document.getElementById("creator-container");

    const creatorBox = document.createElement('div');
    creatorBox.className = "creator-box";

    for (const field of template){
        const id = `${field["id"]}-${crypto.randomUUID()}`;
        const label = field["label"];
        const type = field["type"];
        const mandatory = field["mandatory"];

        const input = buildInput(type, id);
        creatorBox.appendChild(buildRow(input, label, mandatory));
    }

    buildAddAndDeleteButton(container, creatorBox, isFirst, buildCreatorUi);

    container.appendChild(creatorBox);
}


export function getTemplate() {
    return template;
}
