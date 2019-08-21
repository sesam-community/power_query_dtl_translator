import axios from 'axios'

const instance = axios.create ({
    baseURL: 'http://localhost:5000/',
    timeout: 50000
})
// 'https://nfspeed-backend-dot-redfairhair.appspot.com/'

const getResource = (url) => {
    return instance.get(url)
        .then(result => {
            return result.data
        })
        .catch(error => {
            // eslint-disable-next-line no-console
            console.log(error)
            return error
        })
}

export default {
    getResource
}