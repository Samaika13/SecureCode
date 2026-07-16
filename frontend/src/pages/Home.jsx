import { useState } from "react";

import RepositoryForm from "../components/RepositoryForm";
import Results from "../components/Results";

function Home() {

    const [scanResults, setScanResults] = useState(null);

    return (

        <div className="home">

            <div className="hero">

                <h1>🛡️ SecureCode AI</h1>

                <p>
                    AI-powered Static Application Security Testing
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