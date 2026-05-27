console.log("JS Loaded Successfully");
async function downloadPPT() {

    const reportData = {
        company: client.co,
        score: score().overall,
        stage: bandFor(score().overall),
        people: score().byDim.People,
        process: score().byDim.Process,
        data: score().byDim.Data,
        technology: score().byDim.Technology
    };

    const response = await fetch(
        "https://demand-planning-app-nz8x.onrender.com/generate-ppt",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(reportData)
        }
    );

    const blob = await response.blob();

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;
    a.download = "Demand_Planning_Report.pptx";

    document.body.appendChild(a);

    a.click();

    a.remove();
}