import "./LoadingOverlay.css";

function LoadingOverlay({ visible }) {

    if (!visible) return null;

    return (
        <div className="loading-overlay">

            <div className="loading-box">

                <div className="spinner"></div>

                <h2>Scanning Repository...</h2>

                <p>
                    Running static security analysis.
                    This may take a few moments.
                </p>

            </div>

        </div>
    );
}

export default LoadingOverlay;