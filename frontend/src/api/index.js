import config from '../config';

const api = {
  get: function(endpoint, params = {}) {
    let query = Object.keys(params)
      .map(k => encodeURIComponent(k) + '=' + encodeURIComponent(params[k]))
      .join('&');
    return fetch(`${config.apiUrl}${endpoint}/${ query ? '?' + query : ''}`, {
      }).then(res => {
        if (!res.ok) {
          return Promise.reject('실패');
        }
        return res.json();
      });
  },
  post: function(endpoint, body = {}) {
    return fetch(`${config.apiUrl}${endpoint}`, {
      method: 'POST',
      body: JSON.stringify(body)
    }).then(res => {
      if (!res.ok) {
        return Promise.reject('실패');
      }
      return res.json();
    });
  }
};
export default api;
