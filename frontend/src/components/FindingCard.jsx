import "./FindingCard.css";

function FindingCard({ finding }) {
    return (
        <div className="finding-card">

            <div className="finding-header">

                <span className={`severity ${finding.severity.toLowerCase()}`}>
                    {finding.severity}
                </span>

                <span className="scanner">
                    {finding.scanner}
                </span>

            </div>

            <h3>{finding.message}</h3>

            <p>
                <strong>File:</strong> {finding.file}
            </p>

            <p>
                <strong>Line:</strong> {finding.line}
            </p>

            <p>
                <strong>Keyword:</strong> {finding.keyword}
            </p>

            <p>
                <strong>Confidence:</strong> {finding.confidence}
            </p>

            <p>
                <strong>CWE:</strong> {finding.cwe}
            </p>

            <p className="recommendation">
                💡 {finding.recommendation}
            </p>

        </div>
    );
}

export default FindingCard;