const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");

const recognizeBtn = document.getElementById("recognizeBtn");
const clearBtn = document.getElementById("clearBtn");

const recognizedText = document.getElementById("recognizedText");

const confidence = document.getElementById("confidence");

const loading = document.getElementById("loading");

const copyBtn = document.getElementById("copyBtn");
const downloadBtn = document.getElementById("downloadBtn");

let selectedFile = null;


// Image Preview

imageInput.addEventListener("change", function () {

    selectedFile = this.files[0];

    if (!selectedFile) return;

    preview.src = URL.createObjectURL(selectedFile);

    preview.style.display = "block";

});


// Recognize

recognizeBtn.addEventListener("click", async function () {

    if (!selectedFile) {

        alert("Please select an image.");

        return;

    }

    loading.style.display = "block";

    recognizedText.value = "";

    confidence.innerHTML = "";

    const formData = new FormData();

    formData.append("image", selectedFile);

    try {

        const response = await fetch("/predict", {

            method: "POST",

            body: formData

        });

        const data = await response.json();

        loading.style.display = "none";

        if (data.success) {

            recognizedText.value = data.text;

            confidence.innerHTML =
                "Confidence : " + data.confidence;

        } else {

            recognizedText.value = data.message;

        }

    } catch (error) {

        loading.style.display = "none";

        recognizedText.value = "Server Error.";

    }

});


// Copy

copyBtn.addEventListener("click", function () {

    if (recognizedText.value === "") {

        alert("No text to copy.");

        return;

    }

    navigator.clipboard.writeText(recognizedText.value);

    alert("Copied Successfully!");

});


// Download

downloadBtn.addEventListener("click", function () {

    if (recognizedText.value === "") {

        alert("No text available.");

        return;

    }

    const blob = new Blob(
        [recognizedText.value],
        { type: "text/plain" }
    );

    const a = document.createElement("a");

    a.href = URL.createObjectURL(blob);

    a.download = "Recognized_Text.txt";

    a.click();

});


// Clear

clearBtn.addEventListener("click", function () {

    imageInput.value = "";

    preview.style.display = "none";

    preview.src = "";

    recognizedText.value = "";

    confidence.innerHTML = "";

    selectedFile = null;

});