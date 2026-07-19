import { useState } from "react";
import axios from "axios";

type Props = {
    onIndexed: () => void;
};

const API = "http://127.0.0.1:8000/api/v1";

export default function LandingPage({
    onIndexed,
}: Props) {

    const [path, setPath] = useState("");

    const [loading, setLoading] =
        useState(false);

    const [error, setError] =
        useState("");

    async function handleIndex() {

        setError("");

        if (!path.trim()) {
            setError("Repository path required.");
            return;
        }

        try {

            setLoading(true);

            console.log("Calling /index...");

            const res = await axios.post(
                `${API}/index`,
                {
                    repository_path: path,
                }
            );

            console.log("Index response:", res.data);

            console.log("Calling onIndexed()");

            onIndexed();

        } catch (e: any) {

            console.error(e);

            setError(
                e.response?.data?.detail ??
                "Failed to index repository."
            );

        } finally {

            setLoading(false);

        }

    }

    return (

        <div className="min-h-screen bg-zinc-950 flex items-center justify-center">

            <div className="w-[700px] rounded-xl bg-zinc-900 border border-zinc-800 p-10">

                <h1 className="text-5xl font-bold text-white">

                    CodeAtlas AI

                </h1>

                <p className="text-zinc-400 mt-4">

                    AI-powered Repository Intelligence

                </p>

                <div className="mt-10">

                    <label className="text-zinc-300">

                        Repository Path

                    </label>

                    <input
                        className="w-full mt-2 rounded-lg bg-zinc-800 text-white p-4 outline-none"
                        placeholder="C:\Users\Akanksha\Desktop\chips"
                        value={path}
                        onChange={(e) =>
                            setPath(e.target.value)
                        }
                    />

                </div>

                {

                    error &&

                    <p className="text-red-400 mt-4">

                        {error}

                    </p>

                }

                <button
                    className="mt-8 w-full bg-blue-600 hover:bg-blue-700 transition rounded-lg p-4 text-white font-semibold"
                    onClick={handleIndex}
                >

                    {

                        loading

                            ? "Indexing..."

                            : "Index Repository"

                    }

                </button>

                <div className="mt-10 text-zinc-500">

                    Supported

                    <br />

                    ✓ Python

                    <br />

                    ✓ Tree-sitter

                    <br />

                    ✓ Ollama

                    <br />

                    ✓ FAISS

                </div>

            </div>

        </div>

    );

}