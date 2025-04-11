import {buildCreatorUi} from "../../ui/creator/creatorUiBuilder.js";
import {getTemplates} from "../../storage/storageHandler.js";

export function loadAllCreatorData(inputData) {
    const container = document.getElementById('creator-container');
    const template = getTemplates()["templatePerson"];

    for (const box of container.getElementsByClassName('creator-box')){
        box.remove();
    }

    inputData = inputData["creator"];

    for (let i = 0; i < inputData.length; i++){  // for loop with counter because value and index is needed
        buildCreatorUi(i);
        const subContainer = container.querySelector(`#creator-${i}`);

        const data = {};

        for(const attribute of template){
            const key = attribute["id"];
            data[key] = inputData[i][key];
        }

        for (const key of Object.keys(data)){
            const input = subContainer.querySelector("#" + key);
            let value = data[key];

            if(!value){
                value = "";
            }

            if(Array.isArray(value)){
                input.value = value[0];
            } else {
                input.value = value;
            }
        }
    }
}