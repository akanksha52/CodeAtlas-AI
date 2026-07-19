import { useEffect, useMemo, useState } from "react";
import { ChevronDown, ChevronRight, File, Folder } from "lucide-react";
import { getTree } from "../services/repositoryService";

type FileNode = {
    name: string;
    path: string;
    children: FileNode[];
    isFile: boolean;
};

type Props = {
    onOpenFile: (path: string) => void;
};

function insert(root: FileNode, filePath: string) {
    const parts = filePath.split("/");

    let cur = root;

    parts.forEach((part, idx) => {

        let child = cur.children.find(
            c => c.name === part
        );

        if (!child) {

            child = {
                name: part,
                path: parts.slice(0, idx + 1).join("/"),
                children: [],
                isFile: idx === parts.length - 1,
            };

            cur.children.push(child);

        }

        cur = child;

    });
}

export default function RepositoryTree({
    onOpenFile,
}: Props) {

    const [files, setFiles] = useState<any[]>([]);
    const [open, setOpen] = useState<Record<string, boolean>>({});

    useEffect(() => {

        async function load() {

            const res = await getTree();

            setFiles(res.files);

        }

        load();

    }, []);

    const tree = useMemo(() => {

        const root: FileNode = {
            name: "",
            path: "",
            children: [],
            isFile: false,
        };

        files.forEach((f) => insert(root, f.path));

        return root.children;

    }, [files]);

    function Node({
        node,
        level,
    }: {
        node: FileNode;
        level: number;
    }) {

        if (node.isFile) {

            return (

                <button
                    onClick={() => onOpenFile(node.path)}
                    className="flex w-full items-center gap-2 rounded px-2 py-1 text-left text-sm text-zinc-300 hover:bg-zinc-800"
                    style={{
                        paddingLeft: 12 + level * 16,
                    }}
                >
                    <File size={16} />

                    {node.name}

                </button>

            );

        }

        const expanded = open[node.path] ?? true;

        return (

            <div>

                <button
                    className="flex w-full items-center gap-2 rounded px-2 py-1 text-left text-sm text-zinc-200 hover:bg-zinc-800"
                    style={{
                        paddingLeft: 12 + level * 16,
                    }}
                    onClick={() =>
                        setOpen(prev => ({
                            ...prev,
                            [node.path]: !expanded,
                        }))
                    }
                >

                    {

                        expanded
                            ? <ChevronDown size={15} />
                            : <ChevronRight size={15} />

                    }

                    <Folder
                        size={16}
                        className="text-yellow-400"
                    />

                    {node.name}

                </button>

                {

                    expanded &&
                    node.children
                        .sort((a, b) => Number(a.isFile) - Number(b.isFile))
                        .map(child => (

                            <Node
                                key={child.path}
                                node={child}
                                level={level + 1}
                            />

                        ))

                }

            </div>

        );

    }

    return (

        <div className="h-full overflow-auto">

            <div className="mb-3 text-lg font-semibold text-white">

                Repository

            </div>

            {

                tree.map(node => (

                    <Node
                        key={node.path}
                        node={node}
                        level={0}
                    />

                ))

            }

        </div>

    );

}