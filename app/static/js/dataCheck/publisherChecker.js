import {getTemplate} from "../inputFormTemplates/publisher.js";
import {checkByTemplate} from "./checkHelper.js";


export function checkPublisherData(errorInputs) {
    const template = getTemplate();

    checkByTemplate(errorInputs, template);
}