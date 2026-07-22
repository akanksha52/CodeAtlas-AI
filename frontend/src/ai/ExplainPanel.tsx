import { useState } from "react";
import { explain } from "../services/chatService";

type Props = {
    path: string | null;
};

export default function ExplainPanel({ path }: Props) {
    console.log("Explain path:", path);
    const [text, setText] = useState("");
    const [loading, setLoading] = useState(false);

    async function runExplain() {
        if (!path) return;

        setLoading(true);

        try {
            const res = await explain(path);
            setText(res.explanation);
        } catch (err) {
            console.error(err);
            setText("Failed to generate explanation.");
        } finally {
            setLoading(false);
        }
    }

    return (
        <div className="flex flex-col flex-1 min-h-0 border-b border-zinc-800">

            {/* Fixed Header */}
            <div className="p-4 shrink-0">

                <button
                    disabled={!path || loading}
                    onClick={runExplain}
                    className="w-full rounded bg-blue-600 p-2 text-white hover:bg-blue-700 disabled:opacity-40"
                >
                    {loading ? "Explaining..." : "Explain Current File"}
                </button>

            </div>

            {/* Scrollable Explanation */}
            <div className="flex-1 min-h-0 overflow-y-auto px-4 pb-4">

                {!text && !loading && (
                    <p className="text-sm text-zinc-500">
                        Click <strong>Explain Current File</strong> to generate an AI explanation.
                    </p>
                )}

                {loading && (
                    <p className="text-sm text-zinc-400">
                        🤖 Generating explanation...
                    </p>
                )}

                {text && (
                    <div className="whitespace-pre-wrap break-words text-sm leading-7 text-zinc-300">
                        {text}
                    </div>
                )}

            </div>

        </div>
    );
}