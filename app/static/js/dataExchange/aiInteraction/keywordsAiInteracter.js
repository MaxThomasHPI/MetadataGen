export async function askForKeywordsSuggestion(name, description) {
    const url = "/get_keywords_suggestion";

    const payload = {
        "name": name,
        "description": description,
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
                throw new Error('Error while asking for keywords suggestion!');
            }
            return result.json();
        })
}