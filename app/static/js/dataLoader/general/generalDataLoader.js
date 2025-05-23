import {getTemplates} from "../../storage/storageHandler.js";

export function loadGeneralData(inputData) {
    const template = getTemplates()["templateGeneral"];
    const container = document.getElementById('general-container');

    const data = {};

    for(const attribute of template){
        const key = attribute["id"];
        data[key] = inputData[key];
    }
    for (const key of Object.keys(data)){
        const input = container.querySelector("#" + key);
        let value = inputData[key];

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