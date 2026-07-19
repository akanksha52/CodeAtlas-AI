import Editor from "@monaco-editor/react";

type Props = {
    path: string | null;
    language: string;
    content: string;
};

export default function FileViewer({
    path,
    language,
    content,
}: Props) {
    if (!path) {
        return (
            <div className="flex h-full items-center justify-center bg-zinc-950 text-zinc-500">
                Select a file from the repository.
            </div>
        );
    }

    return (
        <div className="h-full flex flex-col bg-zinc-950">

            <div className="h-10 border-b border-zinc-800 flex items-center px-4 text-sm text-zinc-300">
                {path}
            </div>

            <div className="flex-1">
                <Editor
                    height="100%"
                    language={language || "plaintext"}
                    value={content}
                    theme="vs-dark"
                    options={{
                        readOnly: true,
                        minimap: {
                            enabled: false,
                        },
                        fontSize: 14,
                        scrollBeyondLastLine: false,
                        automaticLayout: true,
                    }}
                />
            </div>

        </div>
    );
}