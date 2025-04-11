import {getTemplates} from "../../storage/storageHandler.js";
import {buildAddAndDeleteButton, buildInput, buildRow} from "../helper/helper.js";

export function buildCreatorUi(number) {
    const container = document.getElementById("creator-container");
    const template = getTemplates()["templatePerson"];

    const creatorBox = document.createElement('div');
    creatorBox.className = "creator-box";
    creatorBox.id = "creator-" + number;

    for (const field of template){
        const label = field["id"];
        const type = field["type"];
        const mandatory = field["mandatory"];

        const input = buildInput(type, label);
        creatorBox.appendChild(buildRow(input, label, mandatory));
    }

    buildAddAndDeleteButton(container, creatorBox, number, buildCreatorUi);

    container.appendChild(creatorBox);
}