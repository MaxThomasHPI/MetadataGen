import {loadInputWrapper} from "./loaderHelper.js";


export function loadGeneralData(inputData) {
    const container = document.getElementById('general-container');
    loadInputWrapper(container, inputData);
}