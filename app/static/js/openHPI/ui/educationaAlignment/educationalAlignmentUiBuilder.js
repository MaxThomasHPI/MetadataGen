import {getFrameworks} from "../../../storage/storageHandler.js";
import {buildFrameworkSelect} from "../../../ui/helper/frameworkHelper.js";
import {askForEducationalAlignmentSuggestion} from "../../../dataExchange/aiInteraction/educationalAlignmentAiInteracter.js";

export function buildEducationalAlignmentUi(data){
    const container = document.getElementById("edAlign-container");
    const edAlignFrameworks = getFrameworks()["educationalAlignment"];

    buildFrameworkSelect(edAlignFrameworks, container, "educationalAlignment", 0);
    buildSuggestionButton(container, data);
}


function buildSuggestionButton(container, data) {
    const optCol = container.getElementsByClassName('optional-col')[0];

    const btn = document.createElement('button');
    btn.textContent = "Get Suggestion";

    btn.onclick = async function () {
        const framework = document.getElementById('educationalAlignment-select-0').value;

        const suggestion = await askForEducationalAlignmentSuggestion(data["name"], data["description"], framework);

        const name = `${suggestion[0].name[0].name}@${framework}`;

        const selectedLabel = document.getElementById('selected-educationalAlignment-0');

        selectedLabel.textContent = name;
    }

    optCol.appendChild(btn);
}