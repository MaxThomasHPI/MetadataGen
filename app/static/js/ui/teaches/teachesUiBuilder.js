import {getFrameworks} from "../../storage/storageHandler.js";
import {buildFrameworkSelect} from "../helper/frameworkHelper.js";
import {buildAddAndDeleteButton} from "../helper/helper.js";
import {collectGeneralData} from "../../dataCollect/general/generalDataCollector.js";
import {askForTeachesSuggestion} from "../../dataExchange/aiInteraction/teachesAiInteracter.js";
import {loadTeachesData} from "../../dataLoader/teaches/teachesDataLoader.js";


export function buildTeachesUi(number) {
    const container = document.getElementById("teaches-container");

    const box = document.createElement('div');
    box.className = "teaches-box";
    box.id = `teaches-${number}`;

    const frameworks = getFrameworks()["teaches"];
    buildFrameworkSelect(frameworks, box, "teaches", number);

    container.appendChild(box);

    buildAddAndDeleteButton(container, box, number, buildTeachesUi);

    if(number === 0){
        buildSuggestionButton(container);
    }
}


function buildSuggestionButton(container) {  // add this at the top: 4 suggestions will be made, all 4 shall be shown
                                            // separate teaches boxes!
    const optCol = container.getElementsByClassName('optional-col')[0];

    const btn = document.createElement('button');
    btn.textContent = "Get Suggestion";

    btn.onclick = async function () {
        const framework = document.getElementById('teaches-select-0').value;
        const generalData = collectGeneralData({});
        const suggestion = await askForTeachesSuggestion(generalData["name"], generalData["description"], framework);

        loadTeachesData({
            "teaches": suggestion
        });
    }

    optCol.appendChild(btn);
}
