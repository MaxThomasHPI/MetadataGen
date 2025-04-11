export async function getTemplates(){
    const url = 'get_templates';

    return await fetch(url)
        .then(response => {
            if(!response.ok){
                throw new Error("Error while getting templates!");
            }
            return response.json();
        })
        .catch(error => {
            console.error(error);
        });
}


export async function getFrameworks(){
    const url = 'get_frameworks';

    return await fetch(url)
        .then(response => {
            if(!response.ok){
                throw new Error("Error while getting frameworks!");
            }
            return response.json();
        })
        .catch(error => {
            console.error(error);
        });
}
