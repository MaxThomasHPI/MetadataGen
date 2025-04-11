export async function askForEducationalLevelSuggestion(name, description, educationalFramework) {
    const url = "/get_educational_level_suggestion";

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
                throw new Error('Error while asking for educational level suggestion!');
            }
            return result.json();
        });
}