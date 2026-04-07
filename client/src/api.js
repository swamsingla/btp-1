import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
});

export async function fetchCatalog() {
  const { data } = await api.get('/catalog');
  return data;
}

export async function fetchGrade(grade) {
  const { data } = await api.get(`/catalog/${grade}`);
  return data;
}

export async function fetchSubject(grade, subject) {
  const { data } = await api.get(`/catalog/${grade}/${subject}`);
  return data;
}

export async function fetchContent(grade, subject, chapter, lang = 'en') {
  const { data } = await api.get(`/content/${grade}/${subject}/${chapter}`, {
    params: { lang },
  });
  return data;
}

export async function searchContent(query, lang = 'en') {
  const { data } = await api.get('/search', {
    params: { q: query, lang },
  });
  return data;
}

export default api;
