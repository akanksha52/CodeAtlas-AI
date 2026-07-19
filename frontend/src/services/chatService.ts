import axios from "axios";

const API = "http://127.0.0.1:8000/api/v1";

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