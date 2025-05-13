import {loadData} from "./dataLoader.js";

export async function catchUpload() {
    document.getElementById('file_upload').onchange = async function (ev){
        let file = ev.target.files[0];

        const readFile = (file) => {
            return new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onload = () => resolve(reader.result);
                reader.onerror = () => reject(reader.error);
                reader.readAsText(file);
            });
        };

        const loaded = await readFile(file);
        //console.log(loaded);
        loadData(JSON.parse(loaded));
    }
}