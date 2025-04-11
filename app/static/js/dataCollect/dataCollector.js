import {collectGeneralData} from "./general/generalDataCollector.js";
import {collectLicenseData} from "./general/licenseDataCollector.js";
import {collectCreatorData} from "./creator/creatorDataCollector.js";
import {collectTeachesData} from "./teaches/teachesDataCollector.js";
import {collectPublisherData} from "./publisher/publisherDataCollector.js";
import {collectEdAlignData} from "./educationalAlignment/educationalAlignmentCollector.js";
import {collectKeywordsData} from "./keywords/keywordsDataCollector.js";
import {collectEducationalLevel} from "./educationalLevel/educationalLevelDataCollector.js";

export function collectAllData() {
    let data = {};

    data = collectGeneralData(data);
    data = collectLicenseData(data);
    data = collectPublisherData(data);
    data = collectCreatorData(data);
    data = collectEdAlignData(data);
    data = collectTeachesData(data);
    data = collectKeywordsData(data);
    data = collectEducationalLevel(data);

    return data;
}