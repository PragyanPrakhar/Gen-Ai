"use client";

import { useState } from "react";

const UploadScreen = ({ onUploadSuccess }) => {
    const [file, setFile] = useState(null);
    const [isUploading, setIsUploading] = useState(false);
    const [error, setError] = useState("");

    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0];
        if (selectedFile && selectedFile.type === "application/pdf") {
            setFile(selectedFile);
            setError("");
        } else {
            setError("Please select a valid PDF file");
            setFile(null);
        }
    };

    const handleUpload = async () => {
        if (!file) {
            setError("Please select a PDF file");
            return;
        }

        setIsUploading(true);
        setError("");

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await fetch("http://localhost:8000/upload", {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                const result = await response.json();
                console.log(result.message);
                onUploadSuccess(file.name);
            } else {
                throw new Error("Upload failed");
            }
        } catch (err) {
            setError("Failed to upload PDF. Please try again.");
            console.error("Upload error:", err);
        } finally {
            setIsUploading(false);
        }
    };

    return (
        <div className="flex items-center justify-center min-h-screen p-4">
            <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-md">
                <div className="text-center mb-8">
                    <h1 className="text-3xl font-bold text-gray-800 mb-2">
                        PDF Chat
                    </h1>
                    <p className="text-gray-600">
                        Upload a PDF to start chatting with it
                    </p>
                </div>

                <div className="space-y-6">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Select PDF File
                        </label>
                        <input
                            type="file"
                            accept=".pdf"
                            onChange={handleFileChange}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                        />
                    </div>

                    {file && (
                        <div className="bg-blue-50 p-3 rounded-md">
                            <p className="text-sm text-blue-800">
                                Selected: {file.name}
                            </p>
                        </div>
                    )}

                    {error && (
                        <div className="bg-red-50 p-3 rounded-md">
                            <p className="text-sm text-red-600">{error}</p>
                        </div>
                    )}

                    <button
                        onClick={handleUpload}
                        disabled={!file || isUploading}
                        className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                    >
                        {isUploading ? (
                            <div className="flex items-center justify-center">
                                <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
                                Uploading...
                            </div>
                        ) : (
                            "Upload PDF"
                        )}
                    </button>
                </div>
            </div>
        </div>
    );
};

export default UploadScreen;
