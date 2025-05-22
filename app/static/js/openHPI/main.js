import {buildUI} from "./ui/uiBuilder.js";
import {getFrameworks, getTemplates} from "../dataExchange/templateFrameworkDownloader.js";
import {storeData} from "../storage/storageHandler.js";

function setupUI() {
    const shortCode = document.getElementById('short-code').value;
    //console.log(shortCode);
    buildUI(shortCode);

}

const templateData = await getTemplates();
const frameworkData = await getFrameworks();

storeData(templateData, frameworkData);

document.getElementById('get-course-info').onclick = function() {
    setupUI();
}
