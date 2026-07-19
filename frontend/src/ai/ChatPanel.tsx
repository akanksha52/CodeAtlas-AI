import { useEffect, useRef, useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Send, Bot, User } from "lucide-react";
import { chat } from "../services/chatService";

type Source = {
    file: string;
    symbol: string;
    type: string;
};

type Message = {
    user: string;
    bot: string;
    sources: Source[];
};

type Props = {
    onOpenFile: (path: string) => void;
};

export default function ChatPanel({ onOpenFile }: Props) 
{
    const [message, setMessage] = useState("");
    const [loading, setLoading] = useState(false);
    const [history, setHistory] = useState<Message[]>([]);

    const bottomRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({
            behavior: "smooth",
        });
    }, [history, loading]);

    async function send() {
        if (!message.trim() || loading) return;

        const prompt = message;
        setMessage("");
        setLoading(true);

        try {
            const res = await chat(prompt);

            setHistory((prev) => [
                ...prev,
                {
                    user: prompt,
                    bot: res.response,
                    sources: res.sources ?? [],
                },
            ]);
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    }

    return (
        <div className="flex flex-col h-full">

            <div className="flex-1 overflow-auto p-4 space-y-6">

                {history.map((m, i) => (

                    <div key={i} className="space-y-3">

                        <div className="flex justify-end">

                            <div className="max-w-[85%] rounded-xl bg-blue-600 p-3 text-white">

                                <div className="flex items-center gap-2 mb-2">
                                    <User size={16} />
                                    <span className="font-semibold">
                                        You
                                    </span>
                                </div>

                                {m.user}

                            </div>

                        </div>

                        <div className="flex">

                            <div className="max-w-[90%] rounded-xl bg-zinc-800 p-3 text-zinc-200">

                                <div className="flex items-center gap-2 mb-3 text-green-400">

                                    <Bot size={16} />

                                    <span className="font-semibold">

                                        CodeAtlas AI

                                    </span>

                                </div>

                                <div className="prose prose-invert max-w-none">

                                    <ReactMarkdown
                                        remarkPlugins={[remarkGfm]}
                                    >
                                        {m.bot}
                                    </ReactMarkdown>

                                </div>

                                {m.sources.length > 0 && (

                                    <div className="mt-5 border-t border-zinc-700 pt-3">

                                        <div className="text-xs text-zinc-400 mb-2">

                                            Sources

                                        </div>
                                            {m.sources.map((s, idx) => (

                                                <button
                                                    key={idx}
                                                    onClick={() => onOpenFile(s.file)}
                                                    className="mb-2 w-full rounded-lg bg-zinc-900 p-3 text-left text-xs hover:bg-zinc-800 transition"
                                                >
                                                    <div className="font-semibold text-blue-400">

                                                        📄 {s.file}

                                                    </div>

                                                    <div className="mt-1">

                                                        {s.symbol}

                                                    </div>

                                                    <div className="text-zinc-500">

                                                        {s.type}

                                                    </div>

                                                </button>

                                            ))}

                                    </div>

                                )}

                            </div>

                        </div>

                    </div>

                ))}

                {loading && (

                    <div className="rounded-lg bg-zinc-800 p-3 text-zinc-400">

                        Thinking...

                    </div>

                )}

                <div ref={bottomRef} />

            </div>

            <div className="border-t border-zinc-800 p-4">

                <div className="flex gap-2">

                    <input
                        className="flex-1 rounded-lg bg-zinc-800 p-3 text-white outline-none"
                        placeholder="Ask anything about this repository..."
                        value={message}
                        onChange={(e) =>
                            setMessage(e.target.value)
                        }
                        onKeyDown={(e) => {
                            if (e.key === "Enter") {
                                send();
                            }
                        }}
                    />

                    <button
                        onClick={send}
                        disabled={loading}
                        className="rounded-lg bg-blue-600 px-4 hover:bg-blue-700 disabled:opacity-40"
                    >
                        <Send
                            size={18}
                            color="white"
                        />
                    </button>

                </div>

            </div>

        </div>
    );
}