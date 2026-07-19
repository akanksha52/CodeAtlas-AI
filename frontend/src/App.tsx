import { useState } from "react";

import LandingPage from "./pages/LandingPage";
import Workspace from "./pages/Workspace";

export default function App() {

    const [indexed, setIndexed] =
        useState(false);

    if (!indexed) {

        return (

            <LandingPage
                onIndexed={() =>
                    setIndexed(true)
                }
            />

        );

    }

    return <Workspace />;

}