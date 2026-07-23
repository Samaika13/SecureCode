import "./RepositoryForm.css";
import { useState } from "react";
import api from "../services/api";
import LoadingOverlay from "./LoadingOverlay";

function RepositoryForm({ onScanComplete }) {

    console.log("onScanComplete:", onScanComplete);

    const [repositoryUrl, setRepositoryUrl] = useState("");
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (event) => {

        event.preventDefault();

        if (!repositoryUrl.trim()) {
            return;
        }

        setLoading(true);

        try {

            const response = await api.post(
                "/scan",
                {
                    repository_url: repositoryUrl
                }
            );

            console.log("Response:", response.data);
            console.log("Callback:", onScanComplete);

            if (typeof onScanComplete === "function") {
                onScanComplete(response.data);
            } else {
                console.error("onScanComplete is not a function!");
            }

        } catch (error) {

            console.log(error);
            console.log(error.response);
            console.log(error.response?.data);

            alert("Failed to scan repository.");

        } finally {

            setLoading(false);

        }

    };

    return (
        <>
            <LoadingOverlay visible={loading} />

            <form onSubmit={handleSubmit}>

                <input
                    type="text"
                    placeholder="Paste GitHub repository URL..."
                    value={repositoryUrl}
                    onChange={(event) =>
                        setRepositoryUrl(event.target.value)
                    }
                />

                <button
                    type="submit"
                    disabled={loading}
                >
                    {loading ? "Scanning..." : "🔍 Scan Repository"}
                </button>

            </form>
        </>
    );
}

export default RepositoryForm;