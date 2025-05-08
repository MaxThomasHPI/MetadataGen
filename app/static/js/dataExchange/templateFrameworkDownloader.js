export async function getTemplates(){
    const url = 'get_templates';

    return await fetch(url)
        .then(response => {
            if(!response.ok){
                throw new Error("Error while getting templates!");
            }
            return response.json();
        })
        .catch(error => {
            console.error(error);
        });
}


export async function getFrameworks(){
    const url = 'get_frameworks';

    return await fetch(url)
        .then(response => {
            if(!response.ok){
                throw new Error("Error while getting frameworks!");
            }
            return response.json();
        })
        .catch(error => {
            console.error(error);
        });
}


export async function getESCOFragment(uri) {
    const url = "/get_esco_fragment";

    const body = {
        "uri": uri
    };

    return await fetch(url, {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "body": JSON.stringify(body)
    })
        .then(response => {
            if(!response.ok){
                throw new Error('Error while fetching ESCO fragment');
            }
            return response.json();
        })
        .catch(error => {
            console.error(error);
        });
}
