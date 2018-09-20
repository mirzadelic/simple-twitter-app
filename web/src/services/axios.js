import axios from 'axios'

var newAxios = axios.create({
  baseURL: process.env.VUE_APP_API_URL
})

export default newAxios
