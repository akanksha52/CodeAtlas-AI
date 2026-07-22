import { useState } from "react";
import ExplainPanel from "../ai/ExplainPanel";
import ChatPanel from "../ai/ChatPanel";
import Header from "../components/Header";
import RepositoryTree from "../components/RepositoryTree";
import FileViewer from "../editor/FileViewer";

import { getFile } from "../services/repositoryService";

type FileData = {
    path: string;
    language: string;
    content: string;
};

export default function Workspace() {
    const [file, setFile] = useState<FileData | null>(null);

    async function openFile(path: string) {
        try {
            const data = await getFile(path);
            setFile(data);
        } catch (err) {
            console.error(err);
        }
    }

    return (
        <div className="h-screen flex flex-col bg-zinc-950 overflow-hidden">

            <Header />

            <div className="flex flex-1 min-h-0 overflow-hidden">

                {/* Repository */}
                <aside className="w-72 shrink-0 border-r border-zinc-800 overflow-y-auto">

                    <RepositoryTree
                        onOpenFile={openFile}
                    />

                </aside>

                {/* Code Editor */}
                <main className="flex-1 min-w-0 min-h-0 overflow-hidden">

                    <FileViewer
                        path={file?.path ?? null}
                        language={file?.language ?? ""}
                        content={file?.content ?? ""}
                    />

                </main>

                {/* AI Panel */}
                <aside className="w-[420px] shrink-0 border-l border-zinc-800 flex flex-col min-h-0 bg-zinc-950">

                    <div className="border-b border-zinc-800 p-4 shrink-0">

                        <h2 className="text-white font-semibold">
                            AI Assistant
                        </h2>

                    </div>

                    <div className="flex-1 min-h-0 flex flex-col overflow-hidden">

                        <ExplainPanel
                            path={file?.path ?? null}
                        />

                        <ChatPanel
                            onOpenFile={openFile}
                        />

                    </div>

                </aside>

            </div>

        </div>
    );
}