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
        <div className="h-screen flex flex-col bg-zinc-950">

            <Header />

            <div className="flex flex-1 flex-col lg:flex-row overflow-hidden">

                <aside className="w-full lg:w-72 h-56 lg:h-auto border-r border-zinc-800 overflow-auto p-4">

                    <RepositoryTree
                        onOpenFile={openFile}
                    />

                </aside>

                <main className="flex-1 overflow-hidden">

                    <FileViewer
                        path={file?.path ?? null}
                        language={file?.language ?? ""}
                        content={file?.content ?? ""}
                    />

                </main>

                <aside className="w-full lg:w-[420px] h-[45vh] lg:h-auto border-l border-zinc-800 flex flex-col bg-zinc-950">
                    <div className="border-b border-zinc-800 p-4">

                        <h2 className="text-white font-semibold">

                            AI Assistant

                        </h2>

                    </div>

                    <ExplainPanel
                        path={file?.path ?? null}
                    />

                    <ChatPanel
                        onOpenFile={openFile}
                    />

                </aside>

            </div>

        </div>
    );
}