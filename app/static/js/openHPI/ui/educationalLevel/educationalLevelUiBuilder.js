import {buildRow} from "../../../ui/helper/helper.js";
import {askForEducationalLevelSuggestion} from "../../../dataExchange/aiInteraction/educationalLevelAiInteractor.js";
import {getFrameworks} from "../../../storage/storageHandler.js";
import {loadEducationalLevelData} from "../../../dataLoader/educationalLevel/educationalLevelDataLoader.js";

export function buildEducationalLevelUi(data) {
    const container = document.getElementById('educationalLevel-container');
    const frameworks = getFrameworks()["educationalLevel"];

    buildFrameworkSelect(frameworks, container, data);
    buildDifficultySelect(container, frameworks);
}


function buildFrameworkSelect(frameworks, container, data) {
    const frameworkSelect = document.createElement('select');
    frameworkSelect.id = `educationalLevelFramework-select`;

    for (const key of Object.keys(frameworks)){
        const option = document.createElement('option');
        option.textContent = key;
        option.value = key;

        frameworkSelect.appendChild(option);
    }

    frameworkSelect.onchange = function () {
        document.getElementById('educationalLevel-select').parentElement.parentElement.remove();
        buildDifficultySelect(container, frameworks);
    };

    container.appendChild(buildRow(frameworkSelect, "framework", false));
    buildSuggestionButton(container, frameworkSelect, data);
}


function buildDifficultySelect(container, frameworks) {
    const difficultySelect = document.createElement('select');
    difficultySelect.id = "educationalLevel-select";

    const selectedFramework = document.getElementById('educationalLevelFramework-select').value;

    const framework = frameworks[selectedFramework];

    const noneOption = document.createElement('option');
    noneOption.value = "";
    noneOption.textContent = "None selected";
    difficultySelect.appendChild(noneOption);

    for(const level of framework){
        const option = document.createElement('option');
        option.textContent = level["level"];
        option.value = level["level"];

        difficultySelect.appendChild(option);
    }

    container.appendChild(buildRow(difficultySelect, "educationalLevel", false));
}


function buildSuggestionButton(container, selector, data) {
    const optCol = container.getElementsByClassName('optional-col')[0];

    const btn = document.createElement('button');
    btn.textContent = "Get Suggestion";

    btn.onclick = async function () {
        const framework = selector.value;

        const suggestion = await askForEducationalLevelSuggestion(data["name"], data["description"], framework);

        loadEducationalLevelData(suggestion);
    }

    optCol.appendChild(btn);
}
