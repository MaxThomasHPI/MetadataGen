export function loadInputWrapper(container, inputData) {
    const wrapper = container.getElementsByClassName('input-wrapper');

    for(const singleWrapper of wrapper) {
        const input = singleWrapper.children[0];
        const attributeId = input.id.split("-")[1];
        let value = inputData[attributeId];

        if(!value){
            value = "";
        }
        if(Array.isArray(value)){
            input.value = value[0];
        } else {
            input.value = value;
        }
    }
}
