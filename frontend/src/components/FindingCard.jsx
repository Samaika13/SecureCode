import { useState } from "react";
import "./FindingCard.css";

function FindingCard({ finding }) {

    const [expanded, setExpanded] = useState(false);

    return (

        <div className="finding-card">

            <div
                className="finding-header"
                onClick={() => setExpanded(!expanded)}
            >

                <div>

                    <span
                        className={`severity-badge ${finding.severity.toLowerCase()}`}
                    >
                        {finding.severity}
                    </span>

                    <h2>{finding.message}</h2>

                </div>

                <div className="finding-right">

                    <span>{finding.scanner}</span>

                    <span className="expand-icon">
                        {expanded ? "▲" : "▼"}
                    </span>

                </div>

            </div>

            {expanded && (

                <div className="finding-body">

                    <p><strong>File:</strong> {finding.file}</p>

                    <p><strong>Line:</strong> {finding.line}</p>

                    <p><strong>Keyword:</strong> {finding.keyword}</p>

                    <p><strong>Confidence:</strong> {finding.confidence}</p>

                    <p><strong>CWE:</strong> {finding.cwe}</p>

                    <div className="recommendation">

                        💡 {finding.recommendation}

                    </div>

                </div>

            )}

        </div>

    );

}

export default FindingCard;