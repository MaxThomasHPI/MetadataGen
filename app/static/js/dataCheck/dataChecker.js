import {checkGeneralData} from "./generalChecker.js";
import {checkPublisherData} from "./publisherChecker.js";
import {checkAllCreatorContainer} from "./creatorChecker.js";


export function isInputDataValid() {
    removeAllErrorHighlighting();
    const errorInputs = [];

    checkGeneralData(errorInputs);
    checkPublisherData(errorInputs);
    checkAllCreatorContainer(errorInputs);

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