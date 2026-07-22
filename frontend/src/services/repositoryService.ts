import axios from "axios";

const API = import.meta.env.VITE_API_URL;

export async function getTree() {
    const res = await axios.get(`${API}/tree`);
    return res.data;
}

export async function getStats() {
    const res = await axios.get(`${API}/stats`);
    return res.data;
}

export async function getFile(path: string) {
    const res = await axios.get(`${API}/file`, {
        params: {
            path,
        },
    });

    return res.data;
}

export async function explainFile(path: string) {
    const res = await axios.post(`${API}/explain-file`, {
        path,
    });

    return res.data;
}