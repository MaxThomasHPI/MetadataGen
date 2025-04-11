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

