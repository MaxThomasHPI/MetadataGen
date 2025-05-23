import {buildRow, buildInput} from "../helper/helper.js";
import {getTemplates} from "../../storage/storageHandler.js";

export function buildLicenseUi() {
    const container = document.getElementById("license-container");
    const template = getTemplates()["templateLicense"][0];

    const label = "license";
    const input_id = "identifier";

    const input = buildInput(template["type"], input_id);

    container.appendChild(buildRow(input, label, template["mandatory"]));
}