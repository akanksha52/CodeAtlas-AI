import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000";

export async function sendMessage(message: string) {
  const response = await axios.post(`${API_BASE_URL}/chat`, {
    message,
  });

  return response.data;
}