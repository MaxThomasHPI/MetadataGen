export function isEmpty(object) {
    return Object.keys(object).length === 0
}


export function isValidUrlFormat(url) {
    try{
        new URL(url);
        return true;
    }catch (_) {
        return false;
    }
}


export function isValidDateTime(datetime) {
    const date = new Date(datetime);
    return !isNaN(date.getTime());
}


export function checkByTemplate(errorInputs, template) {
    for(const attribute of template){
        const input = document.getElementById(attribute["id"]);
        const inputValue = input.value;
        if(attribute["mandatory"] && inputValue === ""){
            errorInputs.push(input.parentElement);
            continue;
        }
        checkValidity(errorInputs, attribute, input);
    }
}


export function checkValidity(errorInputs, attribute, input){
    let isValid = true;
    const test = attribute["test"];
    if(test && input.value !== ""){
        switch (test) {
                case "url":
                    isValid = isValidUrlFormat(input.value);
                    break;
                case "date":
                    isValid = isValidDateTime(input.value);
                    break;
        }
    }
    if(!isValid){
        errorInputs.push(input.parentElement);
    }
}
