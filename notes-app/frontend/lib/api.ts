import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
});

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth APIs
export const signup = async (name: string, email: string, password: string, role: string) => {
  const response = await api.post('/auth/signup', { name, email, password, role });
  return response.data;
};

export const login = async (email: string, password: string) => {
  const response = await api.post('/auth/login', { email, password });
  return response.data;
};

export const getMe = async () => {
  const response = await api.get('/auth/me');
  return response.data;
};

// Notes APIs
export const getNotes = async () => {
  const response = await api.get('/notes');
  return response.data;
};

export const createNote = async (title: string, description: string) => {
  const response = await api.post('/notes', { title, description });
  return response.data;
};

export const updateNote = async (id: number, title: string, description: string) => {
  const response = await api.put(`/notes/${id}`, { title, description });
  return response.data;
};

export const deleteNote = async (id: number) => {
  const response = await api.delete(`/notes/${id}`);
  return response.data;
};

export default api;
