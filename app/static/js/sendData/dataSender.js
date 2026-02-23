export async function sendRawData(rawData){
    const url = "/metadata";

    return await fetch(url, {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "body": JSON.stringify(rawData)
    })
        .then(response => {
            if(!response.ok){
                throw new Error("Problem while sending raw data for processing!");
            }
            return response.blob();
        })
        .then(data => {
            const url =window.URL.createObjectURL(data);
            const link =document.createElement('a');
            link.href = url;
            link.download = "metadata.json";
            document.body.appendChild(link);
            link.click();
            link.remove();
            window.URL.revokeObjectURL(url);
        })
        .catch(error => {
            console.error(error);
        });
}