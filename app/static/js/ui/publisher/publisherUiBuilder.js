import {getTemplates} from "../../storage/storageHandler.js";
import {buildInput, buildRow} from "../helper/helper.js";

export function buildPublisherUi() {
    const container = document.getElementById("publisher-container");
    const template = getTemplates()["templateOrganization"];

    for (const field of template){
        const label = field["id"];
        const type = field["type"];
        const mandatory = field["mandatory"];

        const input = buildInput(type, label);
        container.appendChild(buildRow(input, label, mandatory));
    }
}