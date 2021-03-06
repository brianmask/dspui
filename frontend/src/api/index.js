import Axios from 'axios'

Axios.defaults.headers.common['Content-Type'] = 'application/json'

const token = localStorage.getItem('token')

if (token) {
    Axios.defaults.headers.common['Authorization'] = token
}

const API_URL = process.env.NODE_ENV === 'production'
? "/api"
: 'http://localhost:8080/api'

// const API_URL = '/api'
const GET_STORY = `${API_URL}/story/`


export function getStoryTopics () {
    return Axios.get(GET_STORY)
}

export function getStoryBoard (id) {
    return Axios.get(`${GET_STORY}${id}/`)
}