export function collectEdAlignData(data) {
    const selectedEdAlign = document.getElementById('selected-educationalAlignment-0').textContent;
    const name = selectedEdAlign.split("@")[0];

    if(name === "None selected"){
        return data;
    }

    const framework = selectedEdAlign.split("@")[1];

    data["educationalAlignment"] = [{
        "name": name,
        "educationalFramework": framework
    }];

    return data;
}