import {getTemplate} from "../inputFormTemplates/creator.js";
import {checkValidity} from "./checkHelper.js";


export function checkAllCreatorContainer(errorInputs){
    const container = document.getElementsByClassName('creator-box');
    for(const box of container){
        checkCreatorData(errorInputs, box);
    }
}


export function checkCreatorData(errorInputs, container) {
    const template = getTemplate();

    const wrapper = container.getElementsByClassName('input-wrapper');

    for(const singleWrapper of wrapper) {
        const input = singleWrapper.children[0];
        const attributeId = input.id.split("-").slice(0, 2).join("-");

        for (const attribute of template) {
            if (attribute["id"] === attributeId) {
                if (attribute["mandatory"] && input.value === "") {
                    errorInputs.push(input.parentElement);
                    continue;
                }
                checkValidity(errorInputs, attribute, input);
            }
        }
    }
}