import {buildTeachesUi} from "../../ui/teaches/teachesUiBuilder.js";

export function loadTeachesData(inputData) {
    const container = document.getElementById('teaches-container');

    for (let box of container.querySelectorAll('.teaches-box')){
        box.remove();
    }

    const teachesData = inputData["teaches"];

    for (let i = 0; i < teachesData.length; i++){  // for loop with counter because value and index is need
        buildTeachesUi(inputData, i);

        const frameworkSelector = document.getElementById(`teaches-select-${i}`);
        const selectedLabel = document.getElementById(`selected-teaches-${i}`);

        const data = teachesData[i];

        const framework = data["educationalFramework"];
        const name = `${data["name"][0]["name"]}@${data["educationalFramework"]}`;

        frameworkSelector.value = framework;
        frameworkSelector.onchange();
        selectedLabel.textContent = name;
        selectedLabel.setAttribute('conceptUrl', data['conceptUrl']);

    }
}