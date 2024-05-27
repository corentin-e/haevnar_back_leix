import axios from 'axios'

export default function () {
  return {
    getEvents () {
      return axios.get('/events')
    },
  }
}