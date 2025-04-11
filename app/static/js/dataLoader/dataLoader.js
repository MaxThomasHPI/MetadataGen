import {loadGeneralData} from "./general/generalDataLoader.js";
import {loadLicenseData} from "./general/licenseDataLoader.js";
import {loadPublisherData} from "./publisher/publisherDataLoader.js";
import {loadAllCreatorData} from "./creator/creatorDataLoader.js";
import {loadEducationalAlignmentData} from "./educationalAlignment/educationalAlignmentDataLoader.js";
import {loadTeachesData} from "./teaches/teachesDataLoader.js";
import {loadKeywordsData} from "./keywords/keywordsDataLoader.js";
import {loadEducationalLevelData} from "./educationalLevel/educationalLevelDataLoader.js";


export function loadData(inputData) {

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
        loadEducationalAlignmentData(inputData);
    }

    if(Object.keys(inputData).includes("teaches")){
        loadTeachesData(inputData);
    }

    if(Object.keys(inputData).includes("keywords")){
        loadKeywordsData(inputData);
    }

    if(Object.keys(inputData).includes("educationalLevel")){
        loadEducationalLevelData(inputData);
    }

}