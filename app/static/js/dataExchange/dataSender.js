import {collectAllData} from "../dataCollect/dataCollector.js";

export async function submitData() {
    const url = "/generate_metadata";

    const payload = collectAllData();

    if(!payload){
        alert("Error while collecting data from input form!");
    }else {
        await fetch(url, {
            "method": "POST",
            "headers": {
                "Content-Type": "application/json"
            },
            "body": JSON.stringify(payload)
        })
            .then(response => {
                if(!response.ok){
                    throw new Error('Sending raw data error');
                }
            })
            .catch(error => {
                console.error(error);
            })
    }
}