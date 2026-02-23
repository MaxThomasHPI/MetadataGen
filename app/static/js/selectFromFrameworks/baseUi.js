import {getFrameworks} from "./frameworkManager.js";
import {buildFrameworkSelect} from "./frameworkSelector.js";
import {buildAddAndDeleteButton} from "../helper.js";

export function buildBaseUi(group, isFirst= true){
    const container = document.getElementById(`${group}-container`);

    const box = document.createElement('div');
    box.className = `${group}-box`;

    const frameworks = getFrameworks(group);
    buildFrameworkSelect(frameworks, box, group);
    container.appendChild(box);

    buildAddAndDeleteButton(container, box, isFirst, buildBaseUi, group);
}