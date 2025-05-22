import {collectAllData} from "../dataCollector/dataCollector.js";

export async function build_metadata() {
    const url = '/generate_openhpi_metadata_fragments';

    const body = collectAllData();

    return await fetch(url, {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "body": JSON.stringify(body)
    })
        .then(response => {
            if(!response.ok){
                throw new Error("Error while building openHPI fragments!");
            }
            if(response.status === 204){
                alert("No skills or topic selected!");
                return;
            }
            return response.blob();
        })
        .then(data => {
            if(!data){
                return;
            }
            const url = window.URL.createObjectURL(data);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'metadata.zip';
            document.body.appendChild(a);
            a.click();
            a.remove();
            window.URL.revokeObjectURL(url);
        })
        .catch(error => {
           console.error(error);
        });
}