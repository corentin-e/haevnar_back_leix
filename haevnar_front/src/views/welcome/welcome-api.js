import axios from 'axios'

export default function () {
  return {
    getEvents () {
      return axios.get('http://localhost:8000/events')
    },
  }
}