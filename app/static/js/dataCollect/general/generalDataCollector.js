export function collectGeneralData(data) {
    const container = document.getElementById('general-container');
    const inputs = container.getElementsByClassName('input-wrapper');

    for (const input of inputs){
        const value = input.children[0].value
        if(value !== ''){
            data[input.children[0].id] = value;
        }
    }
    return data;
}