import {getFrameworks} from "../../../storage/storageHandler.js";
import {buildFrameworkSelect} from "../../../ui/helper/frameworkHelper.js";
import {buildAddAndDeleteButton} from "../../../ui/helper/helper.js";
import {askForTeachesSuggestion} from "../../../dataExchange/aiInteraction/teachesAiInteracter.js";
import {loadTeachesData} from "../../dataLoader/teaches/teachesDataLoader.js";
import {askForESCOSuggestion} from "../../../dataExchange/escoInteraction/escoInteraction.js";


export function buildTeachesUi(data, number) {

    if(!number){
        number = 0;
    }

    const container = document.getElementById("teaches-container");

    const box = document.createElement('div');
    box.className = "teaches-box";
    box.id = `teaches-${number}`;

    const frameworks = getFrameworks()["teaches"];
    buildFrameworkSelect(frameworks, box, "teaches", number);

    container.appendChild(box);

    buildAddAndDeleteButton(container, box, number, buildTeachesUi);

    if(number === 0){
        buildSuggestionButton(container, data);
    }
}


function buildSuggestionButton(container, data) {  // add this at the top: 4 suggestions will be made, all 4 shall be shown
                                            // separate teaches boxes!
    const optCol = container.getElementsByClassName('optional-col')[0];

    const btn = document.createElement('button');
    btn.textContent = "Get Suggestion";
    btn.id = 'suggest-teaches-btn';

    btn.onclick = async function () {
        const framework = document.getElementById('teaches-select-0').value;

        let suggestion;

        if(framework === "ESCO"){
            suggestion = await askForESCOSuggestion(data["name"], data["description"]);
        }else{
            suggestion = await askForTeachesSuggestion(data["name"], data["description"], framework);
        }

        data["teaches"] = suggestion;

        loadTeachesData(data);

    }

    optCol.appendChild(btn);
}
