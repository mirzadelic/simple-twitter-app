import axios from '@/services/axios'

export default {
  url: 'post/post/',
  getAll (data) {
    return axios.get(this.url, { params: data })
  },
  save (data) {
    var method = 'post'
    var url = this.url
    if (data.id) {
      method = 'patch'
      url += `${data.id}/`
    }

    return axios({
      method: method,
      url: url,
      data: data
    })
  },
  get (id, data) {
    return axios.get(this.url + `${id}/`, { params: data })
  },
  delete (id) {
    return axios.delete(this.url + `${id}/`)
  }
}
