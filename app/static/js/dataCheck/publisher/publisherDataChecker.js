import {getTemplates} from "../../storage/storageHandler.js";
import {isValidUrlFormat} from "../helper/helper.js";

export function checkPublisherData(errorInputs) {
    const template = getTemplates()["templateOrganization"];
    const container = document.getElementById("publisher-container");

    const labels = container.getElementsByTagName("label");

    for(let i = 0; i < labels.length; i++){
        const input = labels[i].parentElement.parentElement
                .getElementsByClassName('input-wrapper')[0].children[0].value;

        if(labels[i].textContent.includes('*') && input === ""){
            errorInputs.push(labels[i].parentElement);
            continue;
        }

        const test = template[i]["test"];
        let testResult = true;
        if(test && input !== ""){
            switch (test) {
                    case "url":
                        testResult = isValidUrlFormat(input);
                        break;
                }
        }

        if(!testResult){
            errorInputs.push(labels[i].parentElement);
        }

    }

    return errorInputs;

}