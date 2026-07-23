import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    Legend
} from "recharts";

import "./SecurityCharts.css";

function SecurityCharts({ findings }) {

    const severityData = [

        {
            name: "High",
            value: findings.filter(f => f.severity === "HIGH").length
        },

        {
            name: "Medium",
            value: findings.filter(f => f.severity === "MEDIUM").length
        },

        {
            name: "Low",
            value: findings.filter(f => f.severity === "LOW").length
        }

    ];

    const colors = [
        "#dc2626",
        "#d97706",
        "#16a34a"
    ];

    const scannerCounts = {};

    findings.forEach(finding => {

        scannerCounts[finding.scanner] =
            (scannerCounts[finding.scanner] || 0) + 1;

    });

    const scannerData = Object.entries(scannerCounts).map(

        ([scanner, count]) => ({

            scanner,

            count

        })

    );

    return (

        <div className="charts-grid">

            <div className="chart-card">

                <h2>Severity Distribution</h2>

                <ResponsiveContainer
                    width="100%"
                    height={300}
                >

                    <PieChart>

                        <Pie
                            data={severityData}
                            dataKey="value"
                            outerRadius={100}
                            label
                        >

                            {severityData.map((entry, index) => (

                                <Cell
                                    key={index}
                                    fill={colors[index]}
                                />

                            ))}

                        </Pie>

                        <Legend />

                        <Tooltip />

                    </PieChart>

                </ResponsiveContainer>

            </div>

            <div className="chart-card">

                <h2>Scanner Distribution</h2>

                <ResponsiveContainer
                    width="100%"
                    height={300}
                >

                    <BarChart data={scannerData} >

                        <CartesianGrid stroke="#374151" />

                        <XAxis 
                            dataKey="scanner"
                            stroke="#d1d5db"
                        />

                        <YAxis
                            stroke="#d1d5db"
                        />

                        <Tooltip />

                        <Bar
                            dataKey="count"
                            fill="#2563eb"
                            radius={[6,6,0,0]}
                        />

                    </BarChart>

                </ResponsiveContainer>

            </div>

        </div>

    );

}

export default SecurityCharts;