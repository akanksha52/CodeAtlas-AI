import { BrainCircuit } from "lucide-react";

export default function Header() {
    return (
        <header className="h-16 border-b border-zinc-800 bg-zinc-950 flex items-center px-6 gap-6">

            {/* Logo */}
            <div className="flex items-center gap-3">

                <BrainCircuit
                    className="text-blue-500"
                    size={28}
                />

                <div>

                    <h1 className="text-white font-bold text-xl">
                        CodeAtlas
                    </h1>

                    <p className="text-xs text-zinc-400">
                        AI Repository Intelligence
                    </p>

                </div>

            </div>

            {/* Search */}
            <div className="flex-1">

                <input
                    className="w-full rounded-lg border border-zinc-700 bg-zinc-900 px-4 py-2 text-white outline-none focus:border-blue-500"
                    placeholder="Search files, classes, functions..."
                />

            </div>

            {/* Status */}
            <div className="flex items-center gap-4">

                <span className="text-green-400 text-sm whitespace-nowrap">
                    ● Ollama Connected
                </span>

            </div>

        </header>
    );
}