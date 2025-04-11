import {getFrameworks, getTemplates} from "./dataExchange/templateFrameworkDownloader.js";
import {storeData} from "./storage/storageHandler.js";
import {buildUI} from "./ui/uiBuilder.js";
import {getExample} from "./dataLoader/example/example.js";
import {loadData} from "./dataLoader/dataLoader.js";


async function setup() {
    const templateData = await getTemplates();
    const frameworkData = await getFrameworks();

    storeData(templateData, frameworkData);
    buildUI();

    const example = getExample(2);
    loadData(example);

}

setup();
