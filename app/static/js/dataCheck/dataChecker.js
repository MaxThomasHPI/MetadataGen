import {checkGeneralData} from "./general/generalDataChecker.js";
import {checkPublisherData} from "./publisher/publisherDataChecker.js";
import {checkCreatorData} from "./creator/creatorDataChecker.js";

export function isInputDataValid() {
    removeAllErrorHighlighting();
    let errorInputs = [];

    errorInputs = checkGeneralData(errorInputs);
    errorInputs = checkPublisherData(errorInputs);
    errorInputs = checkCreatorData(errorInputs);

    if(errorInputs.length > 0){
        highlightErrors(errorInputs);
        return false;
    }
    return true;

}


function highlightErrors(errorInputs){
    for(const input of errorInputs){
        input.classList.add('invalid');
    }
}

function removeAllErrorHighlighting(){
    for(const input of document.getElementsByClassName('invalid')){
        input.classList.remove('invalid');
    }
}
