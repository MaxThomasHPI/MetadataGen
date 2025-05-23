import {getTemplates} from "../../storage/storageHandler.js";

export function loadPublisherData(inputData) {
    const template = getTemplates()["templateOrganization"];
    const container = document.getElementById('publisher-container');

    const data = {};

    for(const attribute of template) {
        const key = attribute["id"];
        data[key] = inputData["publisher"][key];
    }
    for (const key of Object.keys(data)){
        const input = container.querySelector("#" + key);
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