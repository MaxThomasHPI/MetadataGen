import {isEmpty} from "../../helper.js";

export function collectPublisherData(data) {
    let publisherData = {};

    const container = document.getElementById('publisher-container');
    const inputs = container.getElementsByClassName('input-wrapper');

    for (const input of inputs){
        const value = input.children[0].value
        if(value !== ''){
            publisherData[input.children[0].id] = value;
        }
    }
    if(!isEmpty(publisherData)){
        data["publisher"] = publisherData;
    }
    return data;
}