import {isInputDataValid} from "../dataCheck/dataChecker.js";
import {collectGeneralData} from "./generalCollector.js";
import {collectLicenseData} from "./licenseCollector.js";
import {collectPublisherData} from "./publisherCollector.js";
import {collectCreatorData} from "./creatorCollector.js";
import {collectFrameworkData} from "./fromFrameworksCollector.js";
import {collectKeywordsData} from "./keywordsCollector.js";


export function collectData() {
    const isValid = isInputDataValid();

    if(isValid){
        const data = {};

        collectGeneralData(data);
        collectLicenseData(data);
        collectPublisherData(data);
        collectCreatorData(data);
        collectFrameworkData(data, "educationalAlignment");
        collectFrameworkData(data, "teaches");
        collectFrameworkData(data, "educationalLevel");
        collectKeywordsData(data);

        return data;
    } else {
        alert("There are problems with the input data!");
        return null;
    }
}