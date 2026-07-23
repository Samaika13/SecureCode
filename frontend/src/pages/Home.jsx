import { useState } from "react";

import RepositoryForm from "../components/RepositoryForm";
import Results from "../components/Results";

function Home() {

    const [scanResults, setScanResults] = useState(null);

    return (

        <div className="home">

            <div className="hero">

            <h1 className="app-title">
                🛡️ SecureCode
            </h1>

                <p>
                    Analyze GitHub repositories for security vulnerabilities using fast, reliable static analysis.
                </p>

            </div>

            <RepositoryForm
                onScanComplete={setScanResults}
            />

            <Results
                data={scanResults}
            />

        </div>

    );

}

export default Home;