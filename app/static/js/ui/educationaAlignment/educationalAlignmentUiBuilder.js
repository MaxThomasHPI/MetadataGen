import {getFrameworks} from "../../storage/storageHandler.js";
import {buildFrameworkSelect} from "../helper/frameworkHelper.js";
import {askForEducationalAlignmentSuggestion} from "../../dataExchange/aiInteraction/educationalAlignmentAiInteracter.js";
import {collectGeneralData} from "../../dataCollect/general/generalDataCollector.js";


export function buildEducationalAlignmentUi(){
    const container = document.getElementById("edAlign-container");
    const edAlignFrameworks = getFrameworks()["educationalAlignment"];

    buildFrameworkSelect(edAlignFrameworks, container, "educationalAlignment", 0);
    buildSuggestionButton(container);

}


function buildSuggestionButton(container) {
    const optCol = container.getElementsByClassName('optional-col')[0];

    const btn = document.createElement('button');
    btn.textContent = "Get Suggestion";

    btn.onclick = async function () {
        const framework = document.getElementById('educationalAlignment-select-0').value;

        const generalData = collectGeneralData({});
        const suggestion = await askForEducationalAlignmentSuggestion(generalData["name"], generalData["description"], framework);

        const name = `${suggestion[0].name[0].name}@${framework}`;

        const selectedLabel = document.getElementById('selected-educationalAlignment-0');

        selectedLabel.textContent = name;

    }

    optCol.appendChild(btn);
}