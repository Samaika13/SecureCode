import { useState, useEffect, useRef } from "react";
import FindingCard from "./FindingCard";
import "./Results.css";

function Results({ data }) {

    if (!data) return null;

    const highCount = data.findings.filter(
        finding => finding.severity === "HIGH"
    ).length;

    const mediumCount = data.findings.filter(
        finding => finding.severity === "MEDIUM"
    ).length;

    const lowCount = data.findings.filter(
        finding => finding.severity === "LOW"
    ).length;

    const filteredFindings = data.findings.filter((finding) => {

        const query = searchTerm.toLowerCase();

        return (
            finding.file.toLowerCase().includes(query) ||
            finding.message.toLowerCase().includes(query) ||
            finding.keyword.toLowerCase().includes(query) ||
            finding.scanner.toLowerCase().includes(query) ||
            finding.cwe.toLowerCase().includes(query)
        );
    });

    const [visibleCount, setVisibleCount] = useState(25);

    const [searchTerm, setSearchTerm] = useState("");

    const resultsRef = useRef(null);

    useEffect(() => {

        if (data) {
            resultsRef.current?.scrollIntoView({
                behavior: "smooth"
            });
        }
    }, [data]);

    useEffect(() => {
        setVisibleCount(25);
    }, [data]);

    const [selectedSeverity, setSelectedSeverity] = useState("ALL");

    function downloadReport() {

        const json = JSON.stringify(data, null, 2);

        const blob = new Blob(
            [json],
            {
                type: "application/json"
            }
        );

        const url = URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download = `${data.repository}-reportError.json`;

        link.click();

        URL.revokeObjectURL(url);
    }

    return (
        <div
            className="results"
            ref={resultsRef}
        >

            <div className="results-header">

                <button
                    className="download-button"
                    onClick={downloadReport}
                >
                    Download JSON Report
                </button>

                <h1>Scan Results</h1>

                <div className="summary-cards">

                    <div className="summary-card">
                        <h2>{data.total_findings}</h2>
                        <p>Total Findings</p>
                    </div>

                    <div className="summary-card">
                        <h2>{data.repository}</h2>
                        <p>Repository</p>
                    </div>

                </div>

                <div className="severity-summary">

                    <div className="severity-box high-box">
                        <h2>{highCount}</h2>
                        <p>High</p>
                    </div>

                    <div className="severity-box medium-box">
                        <h2>{mediumCount}</h2>
                        <p>Medium</p>
                    </div>

                    <div className="severity-box low-box">
                        <h2>{lowCount}</h2>
                        <p>Low</p>
                    </div>

                </div>

                <div className="search-container">

                    <input
                        type="text"
                        placeholder="Search findings..."
                        value={searchTerm}
                        onChange={(event) =>
                            setSearchTerm(event.target.value)
                        }
                    />

                </div>

                <div className="filter-buttons">

                    <button
                        onClick={() => setSelectedSeverity("ALL")}
                    >
                        All
                    </button>

                    <button
                        onClick={() => setSelectedSeverity("HIGH")}
                    >
                        High
                    </button>

                    <button
                        onClick={() => setSelectedSeverity("MEDIUM")}
                    >
                        Medium
                    </button>

                    <button
                        onClick={() => setSelectedSeverity("LOW")}
                    >
                        Low
                    </button>

                </div>

            </div>

            {filteredFindings.length == 0 && (

                <div className="empty-state">

                    <h2>🎉 No Findings</h2>

                    <p>
                        No vulnerabilities match your current filters.
                    </p>

                </div>
            )}

            {filteredFindings.length > 0 &&

                filteredFindings
                    .slice(0, visibleCount)
                    .map((finding, index) => (

                        <FindingCard
                            key={index}
                            finding={finding}
                        />
                    ))
            }

            {visibleCount < filteredFindings.length && (

                <div className="show-more-container">

                    <button
                        className="show-more-button"
                        onClick={() => setVisibleCount(visibleCount + 25)}
                    >
                        Show More Findings
                    </button>

                </div>

            )}

        </div>
    );
}

export default Results;