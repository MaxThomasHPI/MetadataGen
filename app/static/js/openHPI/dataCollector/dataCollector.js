import {collectTeachesData} from "../../dataCollect/teaches/teachesDataCollector.js";
import {collectEdAlignData} from "../../dataCollect/educationalAlignment/educationalAlignmentCollector.js";
//import {collectKeywordsData} from "./keywords/keywordsDataCollector.js";
//import {collectEducationalLevel} from "../../dataCollect/educationalLevel/educationalLevelDataCollector.js";

export function collectAllData() {
    const data = {};

    collectEdAlignData(data);
    collectTeachesData(data);
    //collectKeywordsData(data);
    //collectEducationalLevel(data);

    return data;
}