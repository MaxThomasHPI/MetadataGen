import {loadInputWrapper} from "./loaderHelper.js";


export function loadPublisherData(inputData) {
    const container = document.getElementById('publisher-container');
    loadInputWrapper(container, inputData["publisher"]);
}