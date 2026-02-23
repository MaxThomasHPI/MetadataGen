import {buildUI} from "./buildForm.js";
import {get_test_data} from "./tests/testData/testData.js";
import {loadData} from "./metadataLoader/loadingManager.js";
import {isInputDataValid} from "./dataCheck/dataChecker.js";


await buildUI();
const test_data = get_test_data();
await loadData(test_data);
//isInputDataValid();
