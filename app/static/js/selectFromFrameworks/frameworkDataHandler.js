export async function getAllToplevel() {
    const url = "/frameworks";

    return await fetch(url)
        .then(response => {
            if(!response.ok){
                throw new Error('Problem while fetching frameworks!');
            }
            return response.json();
        })
        .catch(error => {
            console.error(error)
        });
}


export async function getSubEntries(group, framework, entryUri) {
    const url = "/subentries";

    const data = {
        "group": group,
        "framework": framework,
        "uri": entryUri
    };

    return await fetch(url, {
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "body": JSON.stringify(data)
    })
        .then(response => {
            if(!response.ok){
                throw new Error("Problem while fetching sub-entries!");
            }
            return response.json();
        })
        .catch(error => {
            console.error(error);
    });
}