import {getTemplates} from "../../storage/storageHandler.js";
import {buildInput, buildRow} from "../helper/helper.js";

export function buildGeneralUi() {
    const container = document.getElementById("general-container");
    const template = getTemplates()["templateGeneral"];

    for (const field of template){
        const label = field["id"];
        const type = field["type"];
        const mandatory = field["mandatory"];

        const input = buildInput(type, label);
        container.appendChild(buildRow(input, label, mandatory));
    }
}