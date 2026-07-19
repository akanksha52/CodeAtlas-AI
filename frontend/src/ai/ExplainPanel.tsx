import { useState } from "react";
import { explain } from "../services/chatService";

type Props = {
    path: string | null;
};

export default function ExplainPanel({
    path,
}: Props) {

    const [text, setText] = useState("");
    const [loading, setLoading] = useState(false);

    async function runExplain() {

        if (!path) return;

        setLoading(true);

        try {

            const res = await explain(path);

            setText(res.explanation);

        } finally {

            setLoading(false);

        }

    }

    return (

        <div className="border-b border-zinc-800 p-4">

            <button
                disabled={!path || loading}
                onClick={runExplain}
                className="w-full rounded bg-blue-600 p-2 text-white hover:bg-blue-700 disabled:opacity-40"
            >
                {loading ? "Explaining..." : "Explain Current File"}
            </button>

            <div className="mt-4 whitespace-pre-wrap text-sm text-zinc-300">

                {text}

            </div>

        </div>

    );

}