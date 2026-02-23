import {buildUI} from "../buildForm.js";
import {loadGeneralData} from "./generalLoader.js";
import {loadLicenseData} from "./licenseLoader.js";
import {loadPublisherData} from "./publisherLoader.js";
import {loadAllCreatorData} from "./creatorLoader.js";
import {loadKeywordsData} from "./keywordsLoader.js";
import {loadFrameworksData} from "./frameworksDataLoader.js";


export async function loadData(inputData) {
    while(document.getElementById('main_window').children.length){
        document.getElementById('main_window').children[0].remove();
    }

    await buildUI();

    loadGeneralData(inputData);


    if(Object.keys(inputData).includes("license")){
        loadLicenseData(inputData);
    }
    if(Object.keys(inputData).includes("publisher")){
        loadPublisherData(inputData);
    }
    if(Object.keys(inputData).includes("creator")){
        loadAllCreatorData(inputData);
    }
    if(Object.keys(inputData).includes("educationalAlignment")){
        loadFrameworksData("educationalAlignment", inputData);
    }
    if(Object.keys(inputData).includes("teaches")){
        loadFrameworksData("teaches", inputData);
    }
    if(Object.keys(inputData).includes("keywords")){
        loadKeywordsData(inputData);
    }
    if(Object.keys(inputData).includes("educationalLevel")){
        loadFrameworksData("educationalLevel", inputData);
    }
}