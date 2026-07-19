import { useState } from "react";
import { explainFile } from "../services/repositoryService";

type Props = {
    path: string;
    file: string;
};

export default function FileViewer({
    path,
    file,
}: Props) {

    const [loading, setLoading] =
        useState(false);

    const [explanation, setExplanation] =
        useState("");

    async function handleExplain() {

        if (!path) return;

        setLoading(true);

        const data =
            await explainFile(path);

        setExplanation(
            data.explanation
        );

        setLoading(false);
    }

    return (

        <div>

            <h2>{path}</h2>

            <button
                onClick={handleExplain}
            >
                Explain File
            </button>

            <hr />

            <pre
                style={{
                    whiteSpace: "pre-wrap",
                }}
            >
                {file}
            </pre>

            <hr />

            <h3>Explanation</h3>

            {

                loading

                    ? "Generating..."

                    :

                    <pre
                        style={{
                            whiteSpace:
                                "pre-wrap",
                        }}
                    >
                        {explanation}
                    </pre>

            }

        </div>

    );

}