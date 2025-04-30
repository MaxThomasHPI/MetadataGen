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
                return response.blob();
            })
            .then(response => {
                const url = window.URL.createObjectURL(response);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'metadata.json';
                document.body.appendChild(a);
                a.click();
                a.remove();
                window.URL.revokeObjectURL(url);
            })
            .catch(error => {
                console.error(error);
            })
    }
}