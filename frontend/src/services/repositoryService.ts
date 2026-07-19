import axios from "axios";

const API = "http://127.0.0.1:8000/api/v1";

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