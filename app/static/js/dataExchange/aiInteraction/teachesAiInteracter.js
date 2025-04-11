export async function askForTeachesSuggestion(name, description, educationalFramework) {
    const url = "/get_teaches_suggestion";

    const payload = {
        "name": name,
        "description": description,
        "educationalFramework": educationalFramework
    };

    return await fetch(url, {
            "method": "POST",
            "headers": {
                "Content-Type": "application/json"
            },
            "body": JSON.stringify(payload)
        })
        .then(result => {
            if(!result.ok){
                throw new Error('Error while asking for teaches suggestion!');
            }
            return result.json();
        })
}