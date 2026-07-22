import axios from "axios";

const API = import.meta.env.VITE_API_URL;

export async function chat(message: string) {
    const res = await axios.post(`${API}/chat`, {
        message,
    });

    return res.data;
}

export async function explain(path: string) {
    const res = await axios.post(`${API}/explain-file`, {
        path,
    });

    return res.data;
}