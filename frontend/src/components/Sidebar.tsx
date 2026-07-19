import {
    FolderOpen,
    Database,
    MessageSquare,
    Search
} from "lucide-react";

export default function Sidebar() {

    return (

        <aside className="w-64 bg-zinc-950 border-r border-zinc-800 flex flex-col">

            <div className="p-5">

                <button className="w-full rounded-lg bg-blue-600 hover:bg-blue-700 transition p-3 text-white">

                    Open Repository

                </button>

            </div>

            <nav className="flex flex-col gap-2 px-4">

                <button className="flex items-center gap-3 text-zinc-300 hover:text-white p-3 rounded-lg hover:bg-zinc-900">

                    <FolderOpen size={18} />

                    Repository

                </button>

                <button className="flex items-center gap-3 text-zinc-300 hover:text-white p-3 rounded-lg hover:bg-zinc-900">

                    <Search size={18} />

                    Search

                </button>

                <button className="flex items-center gap-3 text-zinc-300 hover:text-white p-3 rounded-lg hover:bg-zinc-900">

                    <Database size={18} />

                    Statistics

                </button>

                <button className="flex items-center gap-3 text-zinc-300 hover:text-white p-3 rounded-lg hover:bg-zinc-900">

                    <MessageSquare size={18} />

                    AI Chat

                </button>

            </nav>

        </aside>

    );

}