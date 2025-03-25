import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';

// Registro de usuario
const registerUser = async (userData) => {
  try {
    const response = await axios.post(`${API_URL}register/`, userData);
    console.log('Usuario registrado:', response.data);
  } catch (error) {
    console.error('Error registrando usuario:', error);
  }
};

// Login de usuario
const loginUser = async (credentials) => {
  try {
    const response = await axios.post(`${API_URL}token/`, credentials);
    const { access, refresh } = response.data;
    console.log('Tokens recibidos:', access, refresh);
  } catch (error) {
    console.error('Error en login:', error);
  }
};

// Obtener perfil del usuario
const getUserProfile = async (accessToken) => {
  try {
    const response = await axios.get(`${API_URL}profile/`, {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });
    console.log('Perfil del usuario:', response.data);
  } catch (error) {
    console.error('Error obteniendo perfil:', error);
  }
};
