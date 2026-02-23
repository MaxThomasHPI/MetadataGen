import {checkByTemplate} from "./checkHelper.js";
import {getTemplate} from "../inputFormTemplates/generalData.js";


export function checkGeneralData(errorInputs) {
    const template = getTemplate();

    checkByTemplate(errorInputs, template);
}