import "./RepositoryForm.css";
import { useState } from "react";
import api from "../services/api";


function RepositoryForm({ onScanComplete }) {

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
                { repository_url: repositoryUrl }
            );

            onScanComplete(response.data);
        }

        catch (error) {
            alert("Failed to scan repository.");
        }

        finally {
            setLoading(false);
        }
    };

    return (
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
                {loading ? "Scanning..." : "Scan Repository"}
            </button>

        </form>
    );
}

export default RepositoryForm;