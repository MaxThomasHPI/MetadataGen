import {isEmpty} from "../dataCheck/checkHelper.js";
import {collectInputWrapper} from "./collectorHelper.js";


export function collectPublisherData(data) {
    //let publisherData = {};

    const container = document.getElementById('publisher-container');
    data["publisher"] = {};

    collectInputWrapper(container, data["publisher"]);

    /**
    const inputs = container.getElementsByClassName('input-wrapper');

    for (const input of inputs){
        const value = input.children[0].value
        if(value !== ''){
            publisherData[input.children[0].id] = value;
        }
    }
    if(!isEmpty(publisherData)){
        data["publisher"] = publisherData;
    }**/
}