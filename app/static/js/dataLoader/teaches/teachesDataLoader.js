import {buildTeachesUi} from "../../ui/teaches/teachesUiBuilder.js";

export function loadTeachesData(inputData) {
    const container = document.getElementById('teaches-container');

    for (const box of container.getElementsByClassName('teaches-box')){
        box.remove();
    }

    inputData = inputData["teaches"];

    for (let i = 0; i < inputData.length; i++){  // for loop with counter because value and index is need
        buildTeachesUi(i);

        const frameworkSelector = document.getElementById(`teaches-select-${i}`);
        const selectedLabel = document.getElementById(`selected-teaches-${i}`);

        const data = inputData[i];

        const framework = data["educationalFramework"];
        const name = `${data["name"][0]["name"]}@${data["educationalFramework"]}`;

        frameworkSelector.value = framework;
        frameworkSelector.onchange();
        selectedLabel.textContent = name;

    }
}