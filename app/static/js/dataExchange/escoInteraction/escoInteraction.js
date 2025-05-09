export async function askForESCOSuggestion(name, description) {
    const url = "/get_esco_suggestions";

    const body = {
        "name": name,
        "description": description
    }

    return await fetch(url, {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "body": JSON.stringify(body)
    })
        .then(response => {
            if(!response.ok){
                throw new Error("Error with ESCO suggestion!");
            }
            return response.json();
        })
        .catch(error => {
            console.log(error);
        })

}