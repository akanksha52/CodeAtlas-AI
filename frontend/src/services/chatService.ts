import axios from "axios";
import { config } from "../config/config";

export async function sendMessage(message: string) {
  const response = await axios.post(
      `${config.apiBaseUrl}/api/v1/chat`,
      {
          message,
      }
  );

  return response.data;
}