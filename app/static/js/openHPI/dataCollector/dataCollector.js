import {collectTeachesData} from "../../dataCollect/teaches/teachesDataCollector.js";
import {collectEdAlignData} from "../../dataCollect/educationalAlignment/educationalAlignmentCollector.js";

export function collectAllData() {
    const data = {};

    collectEdAlignData(data);
    collectTeachesData(data);

    return data;
}