export function collectInputWrapper(container, data) {
    const inputs = container.getElementsByClassName('input-wrapper');

    for (const input of inputs){
        const attributeName = input.children[0].id.split("-")[1];

        const value = input.children[0].value
        if(value !== ''){
            data[attributeName] = value;
        }
    }
}